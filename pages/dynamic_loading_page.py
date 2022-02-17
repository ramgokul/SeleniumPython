from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DynamicLoadingPage(BasePage):
    _start = (By.CSS_SELECTOR, "div>button")
    _loading_icon = (By.ID, "loading")
    _finish = (By.CSS_SELECTOR, "#finish>h4")

    def __init__(self, driver):
        self.driver = driver

    def load_example(self, number):
        self._visit(f"/dynamic_loading/{number}")
        self._click(self._start)

    def verify_finish_text_present(self):
        self._is_not_displayed(self._loading_icon, timeout=20)
        self._is_displayed(self._finish, timeout=20)
