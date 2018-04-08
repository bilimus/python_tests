# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_python_group_task_1(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False},\
                            firefox_binary="C:/Program Files/FirefoxESR/firefox.exe")
        self.wd.implicitly_wait(60)

    def test_test_python_group_task_1(self):
        success = True
        wd = self.open_page()
        self.login(wd)
        self.open_groups(wd)
        self.create_group(wd)
        self.return_page(wd)
        self.log_out(wd)
        self.assertTrue(success)

    def log_out(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd):
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("sdfer")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("dferty")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("sderty")
        wd.find_element_by_name("submit").click()

    def open_groups(self, wd):
        wd.find_element_by_link_text("groups").click()

    def open_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        return wd

    def login(self, wd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
