import pytest
from assertpy import assert_that

from pages.login_page import LoginPage

# ********************** Invalid login credentials to parametrize ************************
example_params = [("tomsmith", "test"), ("abcd", "xyz")]


@pytest.fixture(params=example_params)
def param_loop(request):
    return request.param
# ********************** Invalid login credentials to parametrize ************************


@pytest.mark.regression
class TestLoginPage:

    @pytest.mark.sanity
    def test_valid_credentials(self, login):
        login.with_("tomsmith", "SuperSecretPassword!")
        is_login_success = login.verify_login_success()
        assert_that(is_login_success).is_true()

    def test_invalid_credentials(self, login, param_loop):
        login.with_(param_loop[0], param_loop[1])
        is_login_failure_msg_displayed = login.verify_login_failure()
        assert_that(is_login_failure_msg_displayed).is_true()
