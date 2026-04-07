import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "http://localhost:5000"
USERNAME = "testuser"
PASSWORD = "Test1234"


def login(page):
    """Helper: log in and navigate to the task page."""
    page.goto(f"{BASE_URL}/login")
    page.fill('input[name="username"]', USERNAME)
    page.fill('input[name="password"]', PASSWORD)
    page.click('button[type="submit"]')
    page.wait_for_load_state("networkidle")


def test_create_task():
    """TC-04: A valid task should appear in the list with status Pending."""
    task_title = "Automated test task"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        login(page)
        # Find and fill the new task input
        page.fill('input[name="title"], input[placeholder*="Task"], input[placeholder*="task"]',
                  task_title)
        page.click('button:has-text("Add Task"), input[value="Add Task"]')
        page.wait_for_load_state("networkidle")
        content = page.content()
        assert task_title in content, (
            f"Expected task '{task_title}' to appear in the task list after creation"
        )
        assert "Pending" in content, (
            "Expected new task to have status 'Pending'"
        )
        browser.close()


def test_create_task_empty_title():
    """TC-05: Empty task title should not create a new task."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        login(page)
        # Count tasks before
        initial_content = page.content()
        task_count_before = initial_content.count("Pending") + \
                            initial_content.count("Working") + \
                            initial_content.count("Done")
        # Submit empty form
        page.click('button:has-text("Add Task"), input[value="Add Task"]')
        page.wait_for_load_state("networkidle")
        # Count tasks after
        after_content = page.content()
        task_count_after = after_content.count("Pending") + \
                           after_content.count("Working") + \
                           after_content.count("Done")
        assert task_count_after == task_count_before, (
            "Expected no new task to be created when title is empty"
        )
        browser.close()


def test_delete_task():
    """TC-06: Delete with confirmation should remove the task from the list."""
    task_title = "Task to delete"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        login(page)
        # Create a task to delete
        page.fill('input[name="title"], input[placeholder*="Task"], input[placeholder*="task"]',
                  task_title)
        page.click('button:has-text("Add Task"), input[value="Add Task"]')
        page.wait_for_load_state("networkidle")
        assert task_title in page.content(), "Task was not created successfully"
        # Handle the confirmation dialog and click Delete
        page.on("dialog", lambda dialog: dialog.accept())
        page.click('button:has-text("Delete"), a:has-text("Delete")')
        page.wait_for_load_state("networkidle")
        assert task_title not in page.content(), (
            f"Expected task '{task_title}' to be removed after deletion"
        )
        browser.close()
