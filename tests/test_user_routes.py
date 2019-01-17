from tests.base import BaseTest
from api.user import views
import json


class UserTestCase(BaseTest):
    def test_returns_error_if_first_name_is_not_valid(self):
        data = {
            "firstname":"",
            "lastname":"Mananu",
            "othernames":"Paul",
            "email":"mderek227@gmail.com",
            "phonenumber":0777123456,
            "username":"mderek",
            "password":"Pass1234"
            }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "A required field is either missing or empty")

    def test_returns_error_if_last_name_is_not_valid(self):
        data = {
            "firstname":"Derrick",
            "lastname":"",
            "othernames":"Paul",
            "email":"mderek227@gmail.com",
            "phonenumber":0777123456,
            "username":"mderek",
            "password":"Pass1234"
            }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "A required field is either missing or empty")

    def test_returns_error_if_other_names_is_missing(self):
        data = {
            "firstname":"Derrick",
            "lastname":"Mananu",
            "email":"mderek227@gmail.com",
            "phonenumber":0777123456,
            "username":"mderek",
            "password":"Pass1234"
            }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "A required field is either missing or empty")

    def test_returns_error_if_email_is_missing(self):
        data = {
        "firstname":"Derrick",
        "lastname":"Mananu",
        "othernames":"Paul",
        "phonenumber":0777123456,
        "username":"mderek",
        "password":"Pass1234"
        }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "A required field is either missing or empty")
    
    def test_returns_error_if_first_name_contains_white_space(self):
        data = {
                "firstname":"Der rick",
                "lastname":"Mananu",
                "othernames":"Paul",
                "email":"mderek227@gmail.com",
                "phonenumber":0777123456,
                "username":"mderek",
                "password":"Pass1234"
                }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "Name must be a string and must not contain spaces")

    def test_returns_error_if_first_name_is_not_a_string(self):
        data = {
                "firstname":25,
                "lastname":"Mananu",
                "othernames":"Paul",
                "email":"mderek227@gmail.com",
                "phonenumber":0777123456,
                "username":"mderek",
                "password":"Pass1234"
                }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "Name must be a string and must not contain spaces")

    def test_returns_error_if_last_name_contains_white_space(self):
        data = {
                "firstname":"Derrick",
                "lastname":"Man anu",
                "othernames":"Paul",
                "email":"mderek227@gmail.com",
                "phonenumber":0777123456,
                "username":"mderek",
                "password":"Pass1234"
                }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "Name must be a string and must not contain spaces")

    def test_returns_error_if_last_name_is_not_a_string(self):
        data = {
                "firstname":"Derrick",
                "lastname":24,
                "othernames":"Paul",
                "email":"mderek227@gmail.com",
                "phonenumber":0777123456,
                "username":"mderek",
                "password":"Pass1234"
                }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "Name must be a string and must not contain spaces")

    def test_returns_error_if_other_names_contains_white_space(self):
        data = {
                "firstname":"Derrick",
                "lastname":"Mananu",
                "othernames":" Pa ul ",
                "email":"mderek227@gmail.com",
                "phonenumber":0777123456,
                "username":"mderek",
                "password":"Pass1234"
                }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "Name must be a string and must not contain spaces")

    def test_returns_error_if_user_name_contains_whitespace(self):
        data = {
                "firstname":"Derrick",
                "lastname":"Mananu",
                "othernames":"Paul",
                "email":"mderek227@gmail.com",
                "phonenumber":0777123456,
                "username":"mde rek",
                "password":"Pass1234"
                }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "Name must be a string and must not contain spaces")

    def test_returns_error_if_phone_number_is_invalid(self):
        data = {
                "firstname":"Derrick",
                "lastname":"Mananu",
                "othernames":"Paul",
                "email":"mderek227@gmail.com",
                "phonenumber":"a777123456",
                "username":"mderek",
                "password":"Pass1234"
                }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "Only numbers are allowed for the phonenumber field")

    def test_returns_error_if_email_is_invalid(self):
        data = {
                "firstname":"Derrick",
                "lastname":"Mananu",
                "othernames":"Paul",
                "email":"mderek227gmail.com",
                "phonenumber":0777123456,
                "username":"mderek",
                "password":"Pass1234"
                }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "Invalid email")

    def test_returns_error_if_password_is_too_short(self):
        data = {
                "firstname":"Derrick",
                "lastname":"Mananu",
                "othernames":"Paul",
                "email":"mderek227@gmail.com",
                "phonenumber":0777123456,
                "username":"mderek",
                "password":"P1234"
                }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],
                         "Password must be atleast 8 characters and should have atleast one number and one capital letter")

    def test_returns_error_if_password_is_weak(self):
        data = {
                "firstname":"Derrick",
                "lastname":"Mananu",
                "othernames":"Paul",
                "email":"mderek227@gmail.com",
                "phonenumber":0777123456,
                "username":"mderek",
                "password":"12345678"
                }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],
                         "Password must be atleast 8 characters and should have atleast one number and one capital letter")

    def test_returns_error_if_user_already_exists(self):
        data = {
                "firstname":"Derrick",
                "lastname":"Mananu",
                "othernames":"Paul",
                "email":"mderek227@gmail.com",
                "phonenumber":0777123456,
                "username":"mderek",
                "password":"Pass1234"
                }
        self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))        
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "User account already exists")

    def test_can_signup_user(self):
        data = {
                "firstname":"Derrick",
                "lastname":"Mananu",
                "othernames":"Paul",
                "email":"mderek227@gmail.com",
                "phonenumber":0777123456,
                "username":"mderek",
                "password":"Pass1234"
                }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 201)
        self.assertEqual(response_data['status'], 201)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['message'], "Your Account was created successfuly")

    def test_can_login_user(self):
        data = {
                "firstname":"Derrick",
                "lastname":"Mananu",
                "othernames":"Paul",
                "email":"mderek227@gmail.com",
                "phonenumber":0777123456,
                "username":"mderek",
                "password":"Pass1234"
                }
        login_data = {
                       "email":"mderek227@gmail.com",
                       "password": "Pass1234"
                     }
        self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(login_data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['message'], "You are now logged-in")

    def test_returns_error_on_failure_to_login(self):
        data = {
                "firstname":"Derrick",
                "lastname":"Mananu",
                "othernames":"Paul",
                "email":"mderek227@gmail.com",
                "phonenumber":0777123456,
                "username":"mderek",
                "password":"Pass1234"
                }
        login_data = {
                       "email":"mderek227@gmail.com",
                       "password": "Pass123"
                     }
        self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(login_data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 403)
        self.assertEqual(response_data['status'], 403)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "Wrong email or password")
