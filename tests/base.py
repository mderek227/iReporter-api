from api.incident.models import incident_db
from api.user.models import user_db
from api.user.controller import create_admin
from api import create_app
import unittest
import json


class BaseTest(unittest.TestCase):
    def setUp(self):
        """
        This method helps setup tests.
        It also initialises the test_client where tests will be run 
        """
        self.app = create_app('Testing')
        self.app = self.app.test_client()

    def tearDown(self):
        user_db.clear()
        incident_db.clear()

    def get_token_admin(self):
        admin_data_login = {
                            "email":"mderek227@gmail.com",
                            "password": "Pass12345"
                            }
        create_admin()
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(admin_data_login))
        data = json.loads(res.data.decode())
        return data['access_token']


    def get_token_user(self):
        user_data = {
                    "firstname":"Derrick",
                    "lastname":"Mananu",
                    "othernames":"Paul",
                    "email":"mderek227@gmail.com",
                    "phonenumber":7777123456,
                    "username":"mderek",
                    "password":"Pass1234"
                    }
        user_data_login = {
                            "email":"mderek227@gmail.com",
                            "password": "Pass1234"
                            }
        self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(user_data))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(user_data_login))
        data = json.loads(res.data.decode())
        return data

    def user_header(self):
        return { 'content_type':"application/json",'Authorization':
                 'Bearer ' + self.get_token_user()['access_token']}

    def admin_header(self):
        return {'content_type':"application/json", 'Authorization':
        'Bearer ' + self.get_token_admin()}



if __name__ == '__main__':
    unittest.main()
