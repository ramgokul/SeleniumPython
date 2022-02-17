import pytest

from pages.dynamic_loading_page import DynamicLoadingPage


@pytest.fixture
def dynamic_loading(driver):
    return DynamicLoadingPage(driver)


@pytest.mark.sanity
def test_dynamic_loading_1(dynamic_loading):
    dynamic_loading.load_example("1")
    dynamic_loading.verify_finish_text_present()


@pytest.mark.regression
def test_dynamic_loading_2(dynamic_loading):
    dynamic_loading.load_example("2")
    dynamic_loading.verify_finish_text_present()
