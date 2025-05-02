import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.bezvavlasy.cz/"
cookiebot_dialog = "#CybotCookiebotDialog"
accept_cookies_btn = "text=Povolit vše"

# odsouhlasení cookies před každým testem
@pytest.fixture(autouse=True)
def accept_cookies_before_each_test(page: Page):
    page.goto(BASE_URL)
    cookie_banner = page.locator(cookiebot_dialog)
    if cookie_banner.is_visible():
        accept_btn = cookie_banner.locator(accept_cookies_btn)
        accept_btn.click()
        expect(cookie_banner).not_to_be_visible()