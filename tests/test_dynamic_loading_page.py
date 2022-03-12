import pytest
from assertpy import assert_that

from pages.dynamic_loading_page import DynamicLoadingPage


@pytest.mark.regression
class TestDynamicLoadingPage:

    @pytest.mark.sanity
    def test_dynamic_loading_1(self, dynamic_loading):
        dynamic_loading.load_example("1")
        finish_text_present = dynamic_loading.verify_finish_text_present()
        assert_that(finish_text_present).is_true()

    def test_dynamic_loading_2(self, dynamic_loading):
        dynamic_loading.load_example("2")
        finish_text_present = dynamic_loading.verify_finish_text_present()
        assert_that(finish_text_present).is_true()
