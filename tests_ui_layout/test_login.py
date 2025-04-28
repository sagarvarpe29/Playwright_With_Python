import pytest
from playwright.sync_api import sync_playwright, Playwright

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("email, password", [("symon.storozhenko@gmail.com", "test123"),
                                             ("test@gmail.com","1234"),
                                             ("sagar@test.com", "sasasa")])

#@pytest.mark.parametrize("email", ["symon.storozhenko@gmail.com",
#                                   "test@gmail.com",
#                                   "sagar@test.com"])

#@pytest.mark.parametrize("password", ["test123",
#                                      "1234",
#                                      "sasasa"])

def test_login(set_up, email, password) -> None:
    page = set_up
    page.click("//button[@data-testid='handle-button' and .//span[text()='Log In']]")
    page.click("//button[@data-testid='signUp.switchToSignUp']")
    page.click("//button[@data-testid='buttonElement' and .//span[text()='Log in with Email']]")
    page.fill('input:below(:text("Email"))', email)
    page.fill('input:below(:text("Password"))', password)
    page.click("//button[@data-testid='buttonElement' and .//span[text()='Log In']]")

    assert page.is_visible("text = Home")