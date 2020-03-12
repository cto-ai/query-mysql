from unittest import TestCase
from unittest.mock import patch

from cto_ai import prompt, sdk

import sys
import os
sys.path.append(os.path.abspath('../src'))
import login


class login_test(TestCase):
    def test_login(self):
        test_login = login.Db_credentials()
        self.assertEqual(test_login.host, "")
        self.assertEqual(test_login.username, "")
        self.assertEqual(test_login.password, "")
        self.assertEqual(test_login.db, "")
        self.assertEqual(test_login.port, "")

    @patch('cto_ai.prompt.input', return_value="normal_input")
    @patch('cto_ai.prompt.password', return_value="password_input")
    def test_normal_inputs(self, mock_prompt1, mock_prompt2):
        test_login = login.Db_credentials()
        test_login.get_credentials()
        self.assertEqual(test_login.host, "normal_input")
        self.assertEqual(test_login.username, "normal_input")
        self.assertEqual(test_login.password, "password_input")
        self.assertEqual(test_login.db, "normal_input")
        self.assertEqual(test_login.port, "normal_input")

    def test_set(self):
        test_login = login.Db_credentials()
        creds = '{"Host":"test_host", "Username":"test_username", "Password":"test_password", "Database":"test_database", "Port":"test_port"}'
        test_login.map_credentials(creds)
        self.assertEqual(test_login.host, "test_host")
        self.assertEqual(test_login.username, "test_username")
        self.assertEqual(test_login.password, "test_password")
        self.assertEqual(test_login.db, "test_database")
        self.assertEqual(test_login.port, "test_port")
    
    
