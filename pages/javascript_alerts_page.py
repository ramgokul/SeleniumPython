from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class JavaScriptAlertsPage(BasePage):

    js_alert = (By.CSS_SELECTOR, "li:nth-child(1)>button")
    js_confirm = (By.CSS_SELECTOR, "li:nth-child(2)>button")
    js_prompt = (By.CSS_SELECTOR, "li:nth-child(3)>button")
    js_result = (By.ID, "result")

    def __init__(self, driver):
        self.driver = driver
        self._visit("/javascript_alerts")

    def click_js_alert(self):
        self._click(self.js_alert)
        assert self._get_alert_text() == "I am a JS Alert"
        self._alert_accept()
        self._is_displayed(self.js_result)
        return self._text(self.js_result)

    def click_js_confirm_ok(self):
        self._click(self.js_confirm)
        assert self._get_alert_text() == "I am a JS Confirm"
        self._alert_accept()
        self._is_displayed(self.js_result)
        return self._text(self.js_result)

    def click_js_confirm_cancel(self):
        self._click(self.js_confirm)
        assert self._get_alert_text() == "I am a JS Confirm"
        self._alert_dismiss()
        self._is_displayed(self.js_result)
        return self._text(self.js_result)

    def click_js_prompt_and_enter_text(self, text):
        self._click(self.js_prompt)
        assert self._get_alert_text() == "I am a JS prompt"
        al = self.driver.switch_to.alert
        al.send_keys(text)
        self._alert_accept()
        self._is_displayed(self.js_result)
        assert self._text(self.js_result) == f"You entered: {text}"
