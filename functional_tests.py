#!/usr/bin/python3
import unittest

from selenium import webdriver


class BasicAppTest(unittest.TestCase):
    """Test the basic app is working"""

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicity_wait(3)

    def tearDown(self):
        self.browser.quit()

    def confirm_admin_page_works(self):
        self.browser.get('localhost:8000')
        self.assertEqual(
            'Welcome to Django',
            self.browser.title
        )


if __name__ == '__main__':
    unittest.main(warnings='ignore')
