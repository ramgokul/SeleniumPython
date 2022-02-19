import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.file_detector import LocalFileDetector
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


import os

from tests import config


@pytest.fixture
def driver(request, cmdopt):

    browser = config.browser_name.lower().strip()
    host = config.host.lower().strip()
    driver_ = None

    if host == "saucelabs" or host == "saucelabs-tunnel":

        if host == "saucelabs":
            sauce_options = {
                "name": request.node.name,
            }
        elif host == "saucelabs-tunnel":
            tunnel_name = config.tunnelidentifier
            sauce_options = {
                "name": request.node.name,
                "tunnel_identifier": tunnel_name
            }

        caps = {
            "browserName": config.browser_name,
            "browserVersion": config.browser_version,
            "platformName": config.platform,
            "acceptInsecureCerts": True,
            "sauce:options": sauce_options
        }
        _credentials = os.environ.get("SAUCE_USERNAME") + ":" + os.environ.get("SAUCE_ACCESS_KEY")
        _url = f"https://{_credentials}@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
        driver_ = webdriver.Remote(command_executor=_url, desired_capabilities=caps)

    elif host == "localhost":
        if browser == "chrome":

            chrome_options = ChromeOptions()
            prefs = {"credentials_enable_service": False,
                     "profile.password_manager_enabled": False}
            chrome_options.add_experimental_option("prefs", prefs)
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_argument("ignore-certificate-errors")
            driver_ = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
            driver_.file_detector = LocalFileDetector()

        elif browser == "firefox":

            firefox_options = FirefoxOptions()
            firefox_options.accept_insecure_certs = True
            driver_ = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)

    driver_.maximize_window()

    yield driver_

    if driver_ is not None:
        if host == "saucelabs" or host == "saucelabs-tunnel":
            sauce_result = "failed" if request.session.testsfailed == 1 else "passed"
            driver_.execute_script("sauce:job-result={}".format(sauce_result))
        driver_.quit()


def pytest_addoption(parser):
    parser.addoption("--baseurl", action="store", default="https://the-internet.herokuapp.com", help="base URL for the AUT")
    parser.addoption("--browser", action="store", default="firefox", help="the name of the browser you want to test with")
    parser.addoption("--host", action="store", default="saucelabs-tunnel", help="where to run your tests : localhost or saucelabs")
    parser.addoption("--browserversion", action="store", default="latest", help="browser version you want to test with")
    parser.addoption("--platform", action="store", default="Windows 10", help="the operating system to run your tests on (saucelabs only)")
    parser.addoption("--tunnelidentifier", action="store", default="ramnath-proxy-tunnel",
                     help="tunnel identifier (saucelabs-tunnel only)")


@pytest.fixture(scope="session")
def cmdopt(request):
    config.base_url = request.config.getoption("--baseurl")
    config.browser_name = request.config.getoption("--browser")
    config.host = request.config.getoption("--host")
    config.browser_version = request.config.getoption("--browserversion")
    config.platform = request.config.getoption("--platform")
    config.tunnelidentifier = request.config.getoption("--tunnelidentifier")
