import pytest
from assertpy import assert_that

from pages.login_page import LoginPage


@pytest.mark.regression
class TestLoginPage:

    @pytest.mark.sanity
    def test_valid_credentials(self, login):
        login.with_("tomsmith", "SuperSecretPassword!")
        is_login_success = login.verify_login_success()
        assert_that(is_login_success).is_true()

    def test_invalid_credentials(self, login):
        login.with_("tomsmith", "test")
        is_login_failure_msg_displayed = login.verify_login_failure()
        assert_that(is_login_failure_msg_displayed).is_true()

