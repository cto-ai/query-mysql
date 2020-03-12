import mysql.connector

from cto_ai import ux, prompt

import src.login as login
from src.logos import logo_print
from src.op_cursor import op_cursor


def main():
    """
    Prompts user for a MySQL database and allows them to print any data they query for
    """
    logo_print()

    db_creds = login.Db_credentials()

    # Prompts
    try:
        db_creds.get_credentials()
    except KeyboardInterrupt:
        print("💤  Exiting Op")
        return

    # Connection
    try:
        connection = make_connection(db_creds)
    except:
        ux.print("❗ Could not connect to " + db_creds.host)
        return

    ux.print("Successfully connected to " + db_creds.host)

    # Select
    try:
        op_cursor(connection)
    except KeyboardInterrupt:
        print("💤  Exiting Op")
    

def make_connection(creds):
    """
    Tries connecting to a given MySQL database.  Factors in potential Slack formating on the host url
    """
    try:
        return mysql.connector.connect(
            host=creds.host,
            user=creds.username,
            passwd=creds.password,
            database=creds.db,
            port=creds.port
        )
    except:
        return mysql.connector.connect(
                host=creds.host.replace("http://", ""),
                user=creds.username,
                passwd=creds.password,
                database=creds.db,
                port=creds.port
            )

if __name__ == "__main__":
    main()
