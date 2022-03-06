from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests import config


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def _find(self, locator):
        return self.driver.find_element(*locator)

    def _visit(self, url):
        if url.startswith("http"):
            self.driver.get(url)
        else:
            self.driver.get(config.base_url.strip("/") + url)

    def _is_displayed(self, locator, timeout=0):

        if timeout > 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(EC.visibility_of_element_located(locator))
            except TimeoutException:
                return False
            else:
                return True
        else:
            try:
                return self._find(locator).is_displayed()
            except NoSuchElementException:
                return False

    def _is_not_displayed(self, locator, timeout=0):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            return False
        else:
            return True

    def _type(self, locator, input_text):
        self._find(locator).send_keys(input_text)

    def _click(self, locator):
        self._find(locator).click()

    def _get_page_title(self):
        return self.driver.title

    def _close(self):
        self.driver.close()

    def _refresh(self):
        self.driver.refresh()

    def _forward(self):
        self.driver.forward()

    def _back(self):
        self.driver.back()

    def _alert_is_present(self, timeout=0):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.alert_is_present())
        except TimeoutException:
            return False
        else:
            return True

    def _alert_accept(self, timeout=0):
        if self._alert_is_present(timeout):
            self.driver.switch_to.alert.accept()
            return True
        else:
            return False

    def _alert_dismiss(self, timeout=0):
        if self._alert_is_present(timeout):
            self.driver.switch_to.alert.dismiss()
            return True
        else:
            return False

    def _get_alert_text(self, timeout=0):
        if self._alert_is_present(timeout):
            _alert_text = self.driver.switch_to.alert.text
            return _alert_text.strip()
        else:
            return False

    def _get_element_text(self, locator):
        return self._find(locator).text.strip()

    def _switch_to_default_content(self):
        self.driver.switch_to.default_content()
