Here's how you could write the pytest automation scripts using playwright.sync_api:


import pytest
from playwright.sync_api import sync_playwright

# Test cases
def test_successful_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://your-url.com/login")
        page.fill('username', 'your-username')
        page.fill('password', 'your-password')
        page.click('text=Login')
        assert page.is_response_status(200)
        browser.close()

def test_incorrect_password():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://your-url.com/login")
        page.fill('username', 'your-username')
        page.fill('password', 'your-incorrect-password')
        page.click('text=Login')
        assert page.is_response_status(401)  # or any other error code
        browser.close()

def test_empty_username():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://your-url.com/login")
        page.fill('password', 'your-password')
        page.click('text=Login')
        assert page.is_response_status(400)  # or any other error code
        browser.close()

def test_locked_account():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://your-url.com/login")
        page.fill('username', 'your-username')
        page.fill('password', 'your-password')
        page.click('text=Login')
        assert page.is_response_status(500)  # or any other error code
        browser.close()

# Edge cases
def test_edge_case_successful_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://your-url.com/login")
        page.fill('username', 'your-username')
        page.fill('password', 'your-password')
        page.click('text=Login')
        assert page.is_response_status(200)
        browser.close()

def test_edge_case_incorrect_password():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://your-url.com/login")
        page.fill('username', 'your-username')
        page.fill('password', 'your-incorrect-password')
        page.click('text=Login')
        assert page.is_response_status(401)  # or any other error code
        browser.close()

def test_edge_case_empty_username():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://your-url.com/login")
        page.fill('password', 'your-password')
        page.click('text=Login')
        assert page.is_response_status(400)  # or any other error code
        browser.close()

def test_edge_case_locked_account():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://your-url.com/login")
        page.fill('username', 'your-username')
        page.fill('password', 'your-password')
        page.click('text=Login')
        assert page.is_response_status(500)  # or any other error code
        browser.close()


Please replace `'your-url.com'`, `'your-username'`, and `'your-password'` with your actual URL, username, and password.

Also, please note that these test cases use the pytest framework. If you haven't used it before, you should install it via pip:

shell
pip install pytest


And for the pytest-playwright plugin, you can install it via pip:

shell
pip install pytest-playwright


You can run these tests via pytest command:

shell
pytest test_playwright_tests.py

