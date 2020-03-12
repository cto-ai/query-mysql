import mysql.connector

from cto_ai import ux, sdk, prompt

SLACK_MAX_CHARACTERS = 2800


def op_cursor(connection) -> None:
    """
    Master control for making queries after a successful connection to a database
    """
    loop = True
    fetch = "One line"
    
    cursor = connection.cursor(buffered = True)

    loop_options = [
        "Make Query",
        "Change Fetch Amount ({:s})".format(fetch),
        "Table List",
        "Column List",
        "Finish"]
    while loop:
        action = prompt.list(
            "action", "\n✨ What would you like to do?", choices = loop_options)
    
        if action == "Make Query":
            try:
                make_query(cursor, fetch)
            except mysql.connector.errors.ProgrammingError as e:
                ux.print("❗{}".format(e))
            except:
                ux.print("❗ Error connecting to server")
        
        if action == "Change Fetch Amount ({:s})".format(fetch):
            if fetch == "One line":
                fetch = "All lines"
            else:
                fetch = "One line"
            
            ux.print(fetch)
            loop_options[1] = "Change Fetch Amount ({:s})".format(fetch)

        if action == "Table List":
            try:
                print_table_list(cursor)
            except:
                ux.print("❗ Failed to get Tables")
        
        if action == "Column List":
            try:
                print_column_list(cursor)
            except:
                ux.print("❗ Failed to get Columns for the requested Table")

        if action == "Finish":
            break                               


def make_query(cursor, fetch: str) -> None:
    """
    Prompts the user for a SQL query, prints the data requested
    """
    select = prompt.input(
        "select", "👉  Please enter your query")

    cursor.execute(select)

    if fetch == "One line":
        data = cursor.fetchone()
        slack_print(str(data))
    else:
        data = cursor.fetchall()
        slack_print(str(data))


def print_table_list(cursor) -> None:
    """
    Prints a list of the tables in the database
    """
    cursor.execute("SHOW TABLES")
    tables = ""
    table_count = 0
    for (table_name,) in cursor:
        tables += table_name + '\n'
        table_count += 1

    slack_print(tables)
    ux.print('{} tables available'.format(table_count))


def print_column_list(cursor) -> None:
    """
    Prints a list of the columns in the database
    """
    table = prompt.input(
        "table", "👉  Which table would you like to retrieve the columns from?")
    show = "SHOW columns FROM {}".format(table)
    cursor.execute(show)
    columns = ""
    for column_name in cursor.fetchall():
        columns += column_name[0] + '\n'

    slack_print(columns[:-1])


def slack_print(s: str) -> None:
    """
    Prints a string in a code block if the Op is ran in Slack, prints normally otherwise
    """
    final_msg = slack_format(s)
    blocks = len(final_msg)
    print_check = True
    if blocks > 1:
        print_check = prompt.confirm(
            "print_check", "✅  The data will be broken up into {} segments.  Continue with print?".format(blocks))
    if print_check:
        for i in final_msg:
            ux.print(i)


def slack_format(s: str) -> list:
    """
    Formats a string for printing based in Interface Type (Slack or Terminal), returns list of separated blocks
    """
    final_msg = []

    interface = sdk.get_interface_type()
    if interface == "slack":
        i = 0
        while i + SLACK_MAX_CHARACTERS < len(s):
            msg = s[i:i + SLACK_MAX_CHARACTERS]
            final_msg.append('```{}```'.format(msg))
            i += SLACK_MAX_CHARACTERS
        final_msg.append('```{}```'.format(s[i:]))

    else:
        final_msg.append(s)

    return final_msg




