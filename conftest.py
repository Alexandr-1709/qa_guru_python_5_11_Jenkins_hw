import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function')
def browser_management():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'
    yield
    browser.quit()
