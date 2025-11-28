# 🎯 Semantic Vision Testing Framework

A beginner-friendly AI-powered visual testing framework that uses Google's Gemini AI to perform intelligent visual assertions on web pages. Perfect for QA engineers who want to automate visual testing without writing complex image comparison code!

## 📋 Table of Contents

- [What is This?](#what-is-this)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Project Structure](#project-structure)
- [How to Write Tests](#how-to-write-tests)
- [Running Tests](#running-tests)
- [Understanding Reports](#understanding-reports)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)

---

## 🤔 What is This?

This framework allows you to write visual tests using **natural language** instead of complex code. Instead of writing pixel-by-pixel comparisons, you can ask questions like:

- "Is the login button visible and clickable?"
- "Does the page look professional with no broken layouts?"
- "Is the main heading clearly visible?"

The AI (Google Gemini) analyzes screenshots and answers your questions, making visual testing much easier!

### ✨ Key Features

- 🧠 **AI-Powered**: Uses Google Gemini 2.0 Flash for intelligent visual analysis
- 🎭 **Playwright Integration**: Automated browser testing with Playwright
- 📸 **Automatic Screenshots**: Captures and saves screenshots for every check
- 📊 **Beautiful HTML Reports**: Generates detailed reports with embedded screenshots and AI responses
- 🐍 **Python & Pytest**: Built with familiar testing tools
- 🔄 **Auto-Cleanup**: Automatically cleans up old screenshots and reports before each run

---

## 📦 Prerequisites

Before you start, make sure you have the following installed on your machine:

### Required Software

1. **Python 3.8 or higher**
   - Check if installed: `python3 --version`
   - Download from: [python.org](https://www.python.org/downloads/)

2. **pip** (Python package manager)
   - Usually comes with Python
   - Check if installed: `pip3 --version`

3. **Google Gemini API Key**
   - You'll need a free API key from Google
   - Get it here: [Google AI Studio](https://aistudio.google.com/app/apikey)
   - ⚠️ **Note**: You may need to sign in with a Google account

---

## 🚀 Installation & Setup

Follow these steps carefully to set up the project:

### Step 1: Clone or Download the Project

```bash
# If using Git
git clone <your-repository-url>
cd Semantic_Vision

# Or download and extract the ZIP file, then navigate to the folder
```

### Step 2: Create a Virtual Environment

A virtual environment keeps your project dependencies isolated.

```bash
# Create virtual environment
python3 -m venv .venv

# Activate it
# On Mac/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

💡 **Tip**: You should see `(.venv)` at the start of your terminal prompt when activated.

### Step 3: Install Dependencies

```bash
# Install all required Python packages
pip install -r requirements.txt

# Install Playwright browsers (this downloads Chrome, Firefox, etc.)
playwright install
```

⏱️ **Note**: The `playwright install` command may take a few minutes as it downloads browser binaries (~300MB).

### Step 4: Configure Your API Key

1. Create a file named `.env` in the project root directory
2. Add your Gemini API key:

```bash
GEMINI_API_KEY=your_actual_api_key_here
```

⚠️ **Important**: 
- Replace `your_actual_api_key_here` with your actual API key
- Never commit the `.env` file to version control (it's already in `.gitignore`)
- Keep your API key secret!

### Step 5: Verify Installation

Run a quick test to make sure everything works:

```bash
pytest tests/test_playground.py
```

If you see tests running and generating reports, you're all set! 🎉

**Expected output:**
```
================== test session starts ==================
...
[Vision Check] 👁️  Analyzing: 'Is the Google logo clearly visible?'...
[Vision Check] 📸 Screenshot saved to: screenshots/...
[Vision Check] 🤖 AI Response: YES. It is prominently displayed...
PASSED

- Generated html report: file:///.../reports/report.html -
=================== 1 passed in X.XXs ===================
```

---

## 📁 Project Structure

Here's what each file and folder does:

```
Semantic_Vision/
├── .env                      # Your API key (create this yourself)
├── .venv/                    # Virtual environment (created during setup)
├── conftest.py               # Pytest configuration and fixtures
├── semantic_vision.py        # Main VisionTester class (the AI magic!)
├── pytest.ini                # Pytest settings (auto-enables logs & reports)
├── requirements.txt          # Python dependencies
├── tests/                    # Your test files go here
│   ├── test_example.py       # Example test file (GitHub homepage)
│   └── test_playground.py    # Playground for quick experiments
├── screenshots/              # Auto-generated screenshots (created when tests run)
├── reports/                  # HTML test reports (created when tests run)
│   └── report.html           # Main test report
└── README.md                 # This file!
```

### Key Files Explained

| File | Purpose |
|------|---------|
| `semantic_vision.py` | Contains the `VisionTester` class that talks to Gemini AI |
| `conftest.py` | Sets up pytest fixtures, cleanup, and HTML report customization |
| `pytest.ini` | Configures pytest to show logs and generate HTML reports automatically |
| `tests/test_*.py` | Your actual test files (must start with `test_`) |

---

## ✍️ How to Write Tests

### Basic Test Structure

Every test file should follow this pattern:

```python
import pytest
from playwright.sync_api import Page

def test_your_test_name(page: Page, vision):
    # 1. Navigate to the page you want to test
    page.goto("https://example.com")
    
    # 2. Perform visual checks using natural language
    vision.assert_visual(page, "Is the main heading visible?")
    vision.assert_visual(page, "Does the page look professional?")
```

### Understanding the Fixtures

#### `page` Fixture
- Provided by `pytest-playwright`
- Gives you a browser page to interact with
- Use it to navigate and interact with websites

#### `vision` Fixture
- Provided by our `conftest.py`
- Gives you access to the `VisionTester` class
- Use it to perform AI-powered visual assertions

### Writing Good Visual Assertions

✅ **Good Examples:**

```python
# Specific and clear
vision.assert_visual(page, "Is the 'Sign In' button visible in the top-right corner?")

# Checking layout quality
vision.assert_visual(page, "Does the page have a clean layout with no overlapping elements?")

# Checking for specific content
vision.assert_visual(page, "Is there a search bar visible on the page?")

# Checking aesthetics
vision.assert_visual(page, "Does the color scheme look professional and cohesive?")
```

❌ **Avoid:**

```python
# Too vague
vision.assert_visual(page, "Does this look good?")

# Too complex (break into multiple checks)
vision.assert_visual(page, "Is the button visible and is the text blue and is it in the center?")

# Asking for exact pixel measurements (AI can't measure precisely)
vision.assert_visual(page, "Is the button exactly 200px wide?")
```

### Example Test File

Create a new file `tests/test_my_website.py`:

```python
import pytest
from playwright.sync_api import Page

def test_homepage_visuals(page: Page, vision):
    """Test the visual appearance of the homepage."""
    
    # Navigate to your website
    page.goto("https://your-website.com")
    
    # Check if the logo is visible
    vision.assert_visual(page, "Is the company logo visible in the header?")
    
    # Check overall layout
    vision.assert_visual(page, "Does the page have a professional appearance with no broken elements?")
    
    # Check for specific content
    vision.assert_visual(page, "Is there a 'Get Started' or 'Sign Up' button visible?")

def test_login_page(page: Page, vision):
    """Test the login page visuals."""
    
    page.goto("https://your-website.com/login")
    
    # Check form elements
    vision.assert_visual(page, "Are there input fields for username and password?")
    vision.assert_visual(page, "Is there a 'Login' or 'Sign In' button?")
    
    # Check for security indicators
    vision.assert_visual(page, "Is there a 'Forgot Password' link visible?")
```

### Using the Playground

The `tests/test_playground.py` file is perfect for quick experiments:

```python
# Just edit these two variables and run!
TARGET_URL = "https://your-site.com"
YOUR_QUESTION = "Is the checkout button clearly visible?"
```

Then run:
```bash
pytest tests/test_playground.py
```

---

## 🏃 Running Tests

### Run All Tests

```bash
pytest
```

This will:
- Run all test files in the `tests/` folder
- Generate screenshots in `screenshots/`
- Create an HTML report in `reports/report.html`
- Show detailed logs in the terminal

### Run a Specific Test File

```bash
pytest tests/test_example.py
```

### Run a Specific Test Function

```bash
pytest tests/test_example.py::test_example_dot_com_visuals
```

### Run with Verbose Output

```bash
pytest -v
```

Shows more detailed information about each test.

### Run in Headed Mode (See the Browser)

```bash
pytest --headed
```

Opens a visible browser window so you can watch the tests run.

### Run with Specific Browser

```bash
# Use Chrome
pytest --browser chromium

# Use Firefox
pytest --browser firefox

# Use Safari (Mac only)
pytest --browser webkit
```

### Useful Command Combinations

```bash
# Run specific test with visible browser and verbose output
pytest tests/test_example.py::test_example_dot_com_visuals --headed -v

# Run all tests with Firefox browser
pytest --browser firefox -v

# Run playground test to quickly test a site
pytest tests/test_playground.py --headed
```

---

## 📊 Understanding Reports

After running tests, open the HTML report:

```bash
# On Mac
open reports/report.html

# On Linux
xdg-open reports/report.html

# On Windows
start reports/report.html
```

### What's in the Report?

The HTML report includes:

1. **Test Summary**
   - Total tests run
   - Passed/Failed counts
   - Duration
   - Environment info (Python version, browser, etc.)

2. **Individual Test Results**
   - Test name and status (✅ PASSED or ❌ FAILED)
   - Click on a test to expand and see:
     - Each visual check with:
       - The question you asked
       - AI's full response
       - **Embedded screenshot** (click "📸 View Screenshot" to expand)
       - URL tested
       - Pass/Fail status with color coding

3. **Screenshots**
   - All screenshots are embedded in the report as base64 images
   - You can also find the original PNG files in the `screenshots/` folder
   - Filenames include timestamp and sanitized prompt for easy identification

### Reading AI Responses

The AI typically responds with:

- **"YES"** - The visual check passed
- **"NO"** - The visual check failed
- **Explanation** - Why it answered yes or no

Example:
```
✅ PASSED: Is the main header clearly visible?
AI Response: YES, the main header "The future of building happens together" 
is clearly visible at the top of the page with large, bold text.
```

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### 1. "GEMINI_API_KEY is not set" Error

**Problem**: The `.env` file is missing or the API key is not set.

**Solution**:
```bash
# Create .env file in project root
echo "GEMINI_API_KEY=your_api_key_here" > .env

# Make sure to replace your_api_key_here with your actual key
```

#### 2. "ModuleNotFoundError: No module named 'pytest_html'" Error

**Problem**: Dependencies are not installed in the current virtual environment.

**Solution**:
```bash
# Make sure virtual environment is activated
source .venv/bin/activate  # Mac/Linux
# or
.venv\Scripts\activate  # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

#### 3. "playwright: command not found" Error

**Problem**: Playwright browsers are not installed.

**Solution**:
```bash
# Make sure virtual environment is activated
source .venv/bin/activate  # Mac/Linux

# Install Playwright browsers
playwright install
```

#### 4. Tests Fail with "Browser not found"

**Problem**: Browser binaries are missing or corrupted.

**Solution**:
```bash
# Reinstall Playwright browsers
playwright install --force
```

#### 5. "No module named 'semantic_vision'" Error

**Problem**: Running tests from wrong directory or virtual environment not activated.

**Solution**:
```bash
# Make sure you're in the project root directory
cd /path/to/Semantic_Vision

# Activate virtual environment
source .venv/bin/activate  # Mac/Linux

# Run tests
pytest
```

#### 6. API Rate Limit Errors

**Problem**: Too many requests to Gemini API.

**Solution**:
- Wait a few minutes before running tests again
- Reduce the number of visual checks in your tests
- Check your API quota at [Google AI Studio](https://aistudio.google.com/)

#### 7. Screenshots Folder is Empty

**Problem**: Tests are not running or failing before screenshots are taken.

**Solution**:
- Check if tests are actually running: `pytest -v`
- Look for errors in the test output
- Make sure the `page.goto()` URL is accessible

#### 8. Report Shows "No Tests Ran"

**Problem**: Test files are not named correctly or not in the right location.

**Solution**:
- Test files must be in the `tests/` folder
- Test files must start with `test_` (e.g., `test_example.py`)
- Test functions must start with `test_` (e.g., `def test_homepage():`)

#### 9. "bad interpreter" Error in Virtual Environment

**Problem**: Virtual environment was created with a path that no longer exists (e.g., after renaming the project folder).

**Solution**:
```bash
# Delete and recreate the virtual environment
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
```

---

## ❓ FAQ

### Q: Do I need to know Python to use this?

**A:** Basic Python knowledge helps, but you can start by copying the example tests and modifying the URLs and questions. The framework is designed to be beginner-friendly!

### Q: How much does the Gemini API cost?

**A:** Google Gemini has a generous free tier (15 requests per minute, 1500 requests per day for Gemini 2.0 Flash). For most testing purposes, you won't hit the limits. Check current pricing at [Google AI Pricing](https://ai.google.dev/pricing).

### Q: Can I test local websites (localhost)?

**A:** Yes! Just use `page.goto("http://localhost:3000")` or whatever your local URL is.

### Q: How accurate is the AI?

**A:** Gemini 2.0 Flash is very accurate for visual checks, but it's not perfect. Always review the reports and screenshots to verify results, especially for critical tests. The AI is best at:
- Detecting presence/absence of elements
- Checking layout quality
- Identifying broken designs
- Verifying text visibility

It's less reliable for:
- Exact color matching
- Precise pixel measurements
- Complex mathematical calculations

### Q: Can I use this in CI/CD pipelines?

**A:** Yes! You can run these tests in GitHub Actions, GitLab CI, Jenkins, etc. Just make sure to:
- Install dependencies in your CI environment
- Set the `GEMINI_API_KEY` as a secret environment variable
- Use headless mode (default)
- Save the HTML report as an artifact

Example GitHub Actions snippet:
```yaml
- name: Run Semantic Vision Tests
  env:
    GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
  run: |
    pip install -r requirements.txt
    playwright install --with-deps
    pytest
- name: Upload Report
  uses: actions/upload-artifact@v3
  with:
    name: test-report
    path: reports/report.html
```

### Q: What browsers are supported?

**A:** Playwright supports:
- Chromium (Chrome/Edge) - **Default**
- Firefox
- WebKit (Safari)

### Q: Can I test mobile views?

**A:** Yes! You can configure viewport size in `conftest.py`:

```python
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 375,   # iPhone width
            "height": 667,  # iPhone height
        }
    }
```

Or use Playwright's device emulation:
```python
page.goto("https://example.com", wait_until="networkidle")
page.set_viewport_size({"width": 375, "height": 667})
```

### Q: How do I debug failing tests?

**A:** 
1. Run with `--headed` to see the browser
2. Check the screenshot in the report
3. Read the AI's explanation for why it failed
4. Add `page.pause()` in your test to pause execution and inspect manually
5. Use `page.screenshot(path="debug.png")` to save additional screenshots

### Q: Can I test PDFs or images?

**A:** This framework is designed for web pages. For PDFs/images, you'd need to display them in a browser first or use a different approach.

### Q: Why are my old screenshots/reports deleted?

**A:** The framework automatically cleans up old screenshots and reports before each test run to avoid clutter. This is configured in `conftest.py`. If you want to keep old reports, comment out the `cleanup_screenshots` and `cleanup_reports` fixtures.

---

## 🎓 Next Steps

Now that you're set up, try:

1. ✅ Run the example tests to see how it works
2. ✅ Edit `tests/test_playground.py` to test your own website
3. ✅ Create your first test file for a website you want to test
4. ✅ Experiment with different types of visual assertions
5. ✅ Review the HTML reports to understand the results
6. ✅ Integrate into your CI/CD pipeline (optional)

---

## 📚 Additional Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Google Gemini API Docs](https://ai.google.dev/docs)
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [pytest-html Plugin](https://pytest-html.readthedocs.io/)

---

## 🤝 Need Help?

If you're stuck:
1. Check the [Troubleshooting](#troubleshooting) section
2. Review the example tests in `tests/test_example.py`
3. Make sure all prerequisites are installed correctly
4. Check that your `.env` file has the correct API key
5. Verify you're in the correct directory with virtual environment activated

---

**Happy Testing! 🚀**

*Built with ❤️ using Python, Playwright, and Google Gemini AI*
