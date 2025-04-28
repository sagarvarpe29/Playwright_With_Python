import pytest
from playwright.sync_api import Playwright

@pytest.fixture
def set_up(page):

    #browser = playwright.chromium.launch(headless = False, slow_mo =5000)
    #context = browser.new_context()

    #page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(10000)
    yield page
    page.close()
