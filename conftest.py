import pytest
from allure_commons._allure import attach
from selenium import webdriver

from selene import Browser, Config
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function')
def browser_management():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1%1234@selenoid:autotests.cloud/wd/hub",
        options=options)

    browser = Browser(Config(driver))

    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'
    yield browser
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
