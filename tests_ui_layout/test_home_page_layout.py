import pytest
from playwright.sync_api import sync_playwright, Playwright
from pom.home_page_elements import HomePage

@pytest.mark.integration
@pytest.mark.regression
def test_about_us_section_verbiage(set_up):
    page = set_up
    # Verifications
    assert page.is_visible(HomePage.celebrating_beauty_header)
    assert page.is_visible(HomePage.celebrating_beauty_header)

@pytest.mark.regression
def test_about_us_section_verbiage2(set_up) -> None:
    page = set_up
    # Verifications
    assert page.is_visible(HomePage.celebrating_beauty_header)
    assert page.is_visible(HomePage.celebrating_beauty_header)