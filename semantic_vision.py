import os
import base64
from io import BytesIO
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class VisionTester:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY is not set. Please set it in .env or pass it to the constructor.")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        
        # Track checks for reporting
        self.checks = []

    def capture_screenshot(self, page):
        """Captures a screenshot from the Playwright page and returns it as bytes."""
        return page.screenshot()

    def ask_ai(self, screenshot_bytes, prompt):
        """Sends the screenshot and prompt to Gemini and returns the response."""
        
        # Create the prompt parts
        contents = [
            prompt + " Answer with just 'YES' or 'NO' and a short explanation if needed.",
            {"mime_type": "image/png", "data": screenshot_bytes}
        ]
        
        response = self.model.generate_content(contents)
        return response.text

    def assert_visual(self, page, prompt):
        """
        Captures a screenshot and asks the AI the prompt.
        Raises an AssertionError if the AI answers 'NO'.
        """
        print(f"\n[Vision Check] 👁️  Analyzing: '{prompt}'...")
        
        # Create screenshots directory
        screenshots_dir = "screenshots"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
            
        # Generate filename based on prompt (sanitized)
        import time
        import re
        timestamp = int(time.time())
        sanitized_prompt = re.sub(r'[^a-zA-Z0-9]', '_', prompt)[:30]
        filename = f"{screenshots_dir}/{timestamp}_{sanitized_prompt}.png"
        
        # Capture and save
        screenshot = self.capture_screenshot(page)
        with open(filename, "wb") as f:
            f.write(screenshot)
        print(f"[Vision Check] 📸 Screenshot saved to: {filename}")

        response_text = self.ask_ai(screenshot, prompt)
        
        print(f"[Vision Check] 🤖 AI Response: {response_text}")
        
        # Basic parsing logic - can be made more robust
        is_positive = "YES" in response_text.upper()
        
        # Track this check for reporting
        check_data = {
            "prompt": prompt,
            "screenshot_path": filename,
            "ai_response": response_text,
            "passed": is_positive,
            "url": page.url
        }
        self.checks.append(check_data)
        
        if not is_positive:
            raise AssertionError(f"Visual assertion failed: {prompt}\nAI Reason: {response_text}")
        
        return True
