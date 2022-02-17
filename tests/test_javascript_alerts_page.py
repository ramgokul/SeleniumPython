import pytest

from pages.javascript_alerts_page import JavaScriptAlertsPage


@pytest.fixture
def js_alerts(driver):
    return JavaScriptAlertsPage(driver)


@pytest.mark.sanity
def test_js_alert(js_alerts):
    assert js_alerts.click_js_alert() == "You successfully clicked an alert"


@pytest.mark.regression
def test_js_confirm_ok(js_alerts):
    assert js_alerts.click_js_confirm_ok() == "You clicked: Ok"


@pytest.mark.regression
def test_js_confirm_cancel(js_alerts):
    assert js_alerts.click_js_confirm_cancel() == "You clicked: Cancel"


@pytest.mark.regression
def test_js_confirm_prompt(js_alerts):
    js_alerts.click_js_prompt_and_enter_text("Ramnath")



