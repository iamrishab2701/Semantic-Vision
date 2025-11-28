import pytest
from playwright.sync_api import Page

def test_example_dot_com_visuals(page: Page, vision):
    page.goto("https://github.com")
    
    # 1. Check for clear visibility of the main header
    vision.assert_visual(page, "Is the main header 'The future of building happens together' clearly visible and legible?")

    # 2. Check for aesthetic issues (subjective)
    vision.assert_visual(page, "Does the page look clean and professional with no broken layout elements?")

    # 3. Check for specific content intent
    vision.assert_visual(page, "Is there a link that clearly indicates it leads to more information?")

def test_negative_case(page: Page, vision):
    """This test is expected to fail to demonstrate the tool's capability."""
    page.goto("https://github.com")
    
    # Intentionally asking for something that isn't there
    try:
        vision.assert_visual(page, "Is 'Sign Up for Github' button is visible with text field?")
    except AssertionError as e:
        print(f"\nCaught expected failure: {e}")
