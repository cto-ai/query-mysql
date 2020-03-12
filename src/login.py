import json

from cto_ai import prompt, sdk, ux


class Db_credentials():

    def __init__(self):
        self.host = ''
        self.username = ''
        self.password = ''
        self.db = ''
        self.port = ''


    def get_credentials(self):
        """
        Gets the host, username, password, database, and port through either individual prompts or a preset secret
        """
        start = prompt.input(
            "start", '👇 Please enter your Host URL (if credentials are configured, enter `set` instead)\n')

        if start.lower() == "set":
            self.set_credentials()

        else:
            self.host = start
            self.get_inputs()


    def get_inputs(self):
        """
        Input prompts for all fields aside from the Host
        """
        self.username = prompt.input(
            "username", "👤  Please enter your Username"
        )
        self.password = self.password_input()
        self.db = prompt.input(
            "database", "👉  Please enter your Database"
        )
        self.port = self.optional_prompt("Port")


    def password_input(self) -> str:
        """
        Password prompt that allows for empty input
        """
        msg = '🔑  Please enter your Password (Enter `none` to skip)'
        password = prompt.password(
            "password", msg)
        if password.lower() == "none":
            return ""
        return password


    def optional_prompt(self, field: str) -> str:
        """
        Input prompt that allows for empty input.  Allows inputting `none` to be consistent with the password prompt
        """
        msg = '👉  Please enter your {} (Enter `none` to skip)'.format(field)
        if sdk.get_interface_type == "slack":
            user_input = prompt.input(
                field, msg)
        else:
            user_input = prompt.input(
                field, msg, allowEmpty=True)
        if user_input.lower() == "none":
            return ""
        return user_input


    def set_credentials(self):
        """
        Gets credentials from a preset secret
        """
        self.set_credentials_instructions()

        creds = prompt.secret(
            "creds", "📂  Please select your pre-set credentials")

        self.map_credentials(creds)


    def set_credentials_instructions(self):
        """
        Prints message on the appropriate format for setting all fields as one
        """
        ux.print("Please set your secrets in the following format:")
        if sdk.get_interface_type() == "slack":
            ux.print(
                '```{"Host": <host>,\n "Username": <username>,\n "Password": <password>,\n "Database": <database>,\n "Port": <port>}```')
        else:
            ux.print(
                '{"Host": <host>,\n "Username": <username>,\n "Password": <password>,\n "Database": <database>,\n "Port": <port>}')


    def map_credentials(self, creds: str):
        """
        Maps fields from a retrieved Secret
        """
        try:
            loaded_creds = json.loads(creds)
        except:
            ux.print("❗ Error: Credentials not in correct format")
            return

        try:
            self.host = loaded_creds["Host"]
            self.username = loaded_creds["Username"]
            self.password = loaded_creds["Password"]
            self.db = loaded_creds["Database"]
            self.port = loaded_creds["Port"]
        except:
            ux.print("❗ Error: Failed to set all fields")
            return
