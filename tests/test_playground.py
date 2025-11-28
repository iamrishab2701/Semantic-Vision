import pytest
from playwright.sync_api import Page

# ---------------------------------------------------------
#  PLAYGROUND: Change these values to test anything!
# ---------------------------------------------------------
TARGET_URL = "https://google.com"
YOUR_QUESTION = "Is the Google logo clearly visible?"
# ---------------------------------------------------------

def test_playground(page: Page, vision):
    print(f"\nVisiting: {TARGET_URL}")
    page.goto(TARGET_URL)
    
    print(f"Asking AI: '{YOUR_QUESTION}'")
    vision.assert_visual(page, YOUR_QUESTION)
    print("Assertion Passed!")
