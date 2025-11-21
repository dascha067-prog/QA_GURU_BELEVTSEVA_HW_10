import pytest
from selene import browser
#
#
# @pytest.fixture(autouse=True)
# def setup_browser():
#     browser.config.window_width = 1200
#     browser.config.window_height = 800
#     browser.config.timeout = 5
#
#     yield
#
#     browser.quit()


@pytest.fixture(autouse=True)
def setup_browser():
    browser.config.window_width = 1200
    browser.config.window_height = 900
    yield
    browser.quit()
