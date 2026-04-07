import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "http://localhost:5000"
USERNAME = "testuser"
PASSWORD = "Test1234"


def test_login_valid():
    """TC-01: Valid login should redirect to the task management page."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"{BASE_URL}/login")
        page.fill('input[name="username"]', USERNAME)
        page.fill('input[name="password"]', PASSWORD)
        page.click('button[type="submit"]')
        page.wait_for_load_state("networkidle")
        assert "login" not in page.url.lower(), (
            f"Expected to leave login page, but URL is: {page.url}"
        )
        assert USERNAME.lower() in page.content().lower(), (
            "Expected username to appear in page after login"
        )
        browser.close()


def test_login_invalid():
    """TC-02: Invalid password should show error and stay on login page."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"{BASE_URL}/login")
        page.fill('input[name="username"]', USERNAME)
        page.fill('input[name="password"]', "WrongPassword99")
        page.click('button[type="submit"]')
        page.wait_for_load_state("networkidle")
        assert "login" in page.url.lower(), (
            f"Expected to stay on login page, but URL is: {page.url}"
        )
        content = page.content().lower()
        assert any(word in content for word in ["invalid", "incorrect", "error", "wrong"]), (
            "Expected an error message to appear on the login page"
        )
        browser.close()


def test_logout():
    """Logout should end the session and redirect to the login page."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # Log in first
        page.goto(f"{BASE_URL}/login")
        page.fill('input[name="username"]', USERNAME)
        page.fill('input[name="password"]', PASSWORD)
        page.click('button[type="submit"]')
        page.wait_for_load_state("networkidle")
        # Now log out
        page.goto(f"{BASE_URL}/logout")
        page.wait_for_load_state("networkidle")
        assert "login" in page.url.lower() or page.url == f"{BASE_URL}/", (
            f"Expected to be redirected to login after logout, but URL is: {page.url}"
        )
        browser.close()
