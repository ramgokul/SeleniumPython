import pytest
from assertpy import assert_that

from pages.login_page import LoginPage


@pytest.fixture
def login(driver):
    return LoginPage(driver)


@pytest.mark.sanity
def test_valid_credentials(login):
    login.with_("tomsmith", "SuperSecretPassword!")
    is_login_success = login.verify_login_success()
    assert_that(is_login_success).is_true()


@pytest.mark.regression
def test_invalid_credentials(login):
    login.with_("tomsmith", "test")
    is_login_failure_msg_displayed =  login.verify_login_failure()
    assert_that(is_login_failure_msg_displayed).is_true()

