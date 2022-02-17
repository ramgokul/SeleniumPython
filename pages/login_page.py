from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    username = (By.ID, "username")
    password = (By.ID, "password")
    login_form = (By.ID, "login")
    login_button = (By.CSS_SELECTOR, ".radius")
    login_success = (By.CSS_SELECTOR, ".flash.success")
    login_failure = (By.CSS_SELECTOR, ".flash.error")

    def __init__(self, driver):
        self.driver = driver
        self._visit("/login")
        assert self._is_displayed(self.login_form, timeout=10)
        print(self._get_page_title())

    def with_(self, username, password):
        self._type(self.username, username)
        self._type(self.password, password)
        self._click(self.login_button)

    def verify_login_success(self):
        return self._is_displayed(self.login_success)

    def verify_login_failure(self):
        return self._is_displayed(self.login_failure)