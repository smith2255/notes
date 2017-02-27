import unittest

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class BasicAppTest(LiveServerTestCase):
    """Test the basic app is working"""

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicity_wait(3)

    def tearDown(self):
        self.browser.quit()

    def confirm_admin_page_works_test(self):
        self.browser.get(self.live_server_url)
        self.assertEqual(
            'Welcome to Django',
            self.browser.title
        )


class ListNoteTest(LiveServerTestCase):
    """Test the basic app is working"""

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicity_wait(3)

    def tearDown(self):
        self.browser.quit()

    def confirm_admin_page_works_test(self):
        self.browser.get(self.live_server_url)
        self.assertEqual(
            'Notes',
            self.browser.title
        )
        self.assertEqual(
            'Notes',
            self.browser.heading
        )
        self.fail('Finish Writing')
