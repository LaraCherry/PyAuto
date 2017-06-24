import unittest
from selenium import webdriver
from reg_page import RegistrationPage
from random import randint


class TestRedistration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()

    def setUp(self):
        RegistrationPage(self.browser).open()

    def test_registration_with_different_passwords(self):
        page = RegistrationPage(self.browser)

        reg_data = {
            'first_name': 'Vova',
            'last_name': 'ZiLvova',
            'email': 'vovan@gmail.com',
            'password': 'pwd3256',
            'confirmation': 'ppwd3256'
        }

        for field, value in reg_data.items():
            page.find_element(field).send_keys(value)
        page.find_element('newsletter_chbx').click()
        page.find_element('register_btn').click()

        self.assertTrue(page.is_password_validation_error)

        # "bla: {} {}".format(arg1,arg2)

    def test_registration_success(self):
        page = RegistrationPage(self.browser)

        reg_data = {
            'first_name': 'Vova',
            'last_name': 'ZiLvova',
            'email': 'vovan+{}@gmail.com'.format(randint(0, 100)),
            'password': 'password1',
            'confirmation': 'password1'
        }

        for field, value in reg_data.items():
            page.find_element(field).send_keys(value)
        page.find_element('newsletter_chbx').click()
        page.find_element('register_btn').click()

        ##########################

        # page.find_element('ACCOUNT_lb').click()
        # page.find_element('Log Out_lnk').click()

    # def log_out(self):
    #
    #     page.find_element('ACCOUNT_lb').click()
    #     page.find_element('Log Out_lnk').click()


