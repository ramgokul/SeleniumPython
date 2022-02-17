import pytest
from pages.login_page import LoginPage


@pytest.fixture
def login(driver):
    return LoginPage(driver)


@pytest.mark.sanity
def test_valid_credentials(login):
    login.with_("tomsmith", "SuperSecretPassword!")
    assert login.verify_login_success()


@pytest.mark.regression
def test_invalid_credentials(login):
    login.with_("tomsmith", "test")
    assert login.verify_login_failure()

