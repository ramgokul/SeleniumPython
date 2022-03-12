import pytest

from pages.javascript_alerts_page import JavaScriptAlertsPage


@pytest.mark.regression
class TestJavascriptAlertsPage:

    @pytest.mark.sanity
    def test_js_alert(self, js_alerts):
        assert js_alerts.click_js_alert() == "You successfully clicked an alert"

    def test_js_confirm_ok(self, js_alerts):
        assert js_alerts.click_js_confirm_ok() == "You clicked: Ok"

    def test_js_confirm_cancel(self, js_alerts):
        assert js_alerts.click_js_confirm_cancel() == "You clicked: Cancel"

    def test_js_confirm_prompt(self, js_alerts):
        js_alerts.click_js_prompt_and_enter_text("Ramnath")



