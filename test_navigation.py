import unittest
from selenium import webdriver
from link import Link
from header import Header
from login_page import LoginPage


class TestNavigation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()

    def test_footer_links(self):
        links = (
            # MAN
            'New Arrivals'
            'Tops & Blouses'
            'Pants & Denim'
            'Dresses & Skirts'
            # WOMAN
        )

        LoginPage(self.browser).open()
        for link in links:
            Link(self.browser, link).hover()
            Link(self.browser, link).click()
            # hover()
            # click()

            self.assertEqual(Header(self.browser.title, link).is_visible)