import os

import pytest
from selenium import webdriver

from framework.config.browser_options import BrowserFactory


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=True,
        help="Run browsers in headless mode",
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Specify which browser to use (comma-separated, e.g., 'chrome,firefox,edge')",
    )


def pytest_generate_tests(metafunc):
    """
    Generate tests for each browser specified in the command line.
    """
    if "driver" in metafunc.fixturenames:
        browsers = metafunc.config.getoption("--browser").split(",")
        metafunc.parametrize("driver", browsers, indirect=True)


@pytest.fixture
def driver(request):
    """
    Fixture to create and return a WebDriver instance based on the selected browser.
    """
    headless = request.config.getoption("--headless")
    browsers = request.config.getoption("--browser").split(",")

    browser_param = getattr(request, "param", browsers[0])

    browser_options = BrowserFactory().get_browser_options(browser_param, headless)

    grid_url = os.environ.get('SELENIUM_GRID_URL', 'http://selenium-hub:4444/wd/hub')

    driver = webdriver.Remote(
        command_executor=grid_url,
        options=browser_options
    )

    yield driver

    driver.quit()
