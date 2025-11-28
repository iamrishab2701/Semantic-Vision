import pytest
import os
import shutil
import base64
from pytest_html import extras

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1280,
            "height": 720,
        }
    }

@pytest.fixture(scope="session", autouse=True)
def cleanup_screenshots():
    """Cleans up the screenshots directory before the test session starts."""
    screenshots_dir = "screenshots"
    if os.path.exists(screenshots_dir):
        # Remove the directory and all its contents
        shutil.rmtree(screenshots_dir)
        print(f"\n[Cleanup] 🧹 Removed old screenshots from: {screenshots_dir}")
    
    # Re-create the directory
    os.makedirs(screenshots_dir)
    print(f"[Cleanup] 🆕 Created fresh screenshots directory: {screenshots_dir}")

@pytest.fixture(scope="session", autouse=True)
def cleanup_reports():
    """Cleans up the reports directory before the test session starts."""
    reports_dir = "reports"
    if os.path.exists(reports_dir):
        shutil.rmtree(reports_dir)
        print(f"[Cleanup] 🧹 Removed old reports from: {reports_dir}")
    
    os.makedirs(reports_dir)
    print(f"[Cleanup] 🆕 Created fresh reports directory: {reports_dir}")

@pytest.fixture
def vision():
    """Fixture to provide VisionTester instance."""
    from semantic_vision import VisionTester
    return VisionTester()

# Hook to add vision check data to HTML report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Add vision check details to the HTML report."""
    outcome = yield
    report = outcome.get_result()
    
    # Only process test calls (not setup/teardown)
    if report.when == "call":
        # Look for VisionTester in the test's local namespace or fixtures
        vision_tester = None
        
        # Try to get from funcargs (fixtures)
        if hasattr(item, 'funcargs'):
            vision_tester = item.funcargs.get('vision')
        
        # If not found in fixtures, try to get from test module globals
        if not vision_tester and hasattr(item, 'module'):
            if hasattr(item.module, 'vision'):
                vision_tester = item.module.vision
        
        if vision_tester and hasattr(vision_tester, 'checks') and vision_tester.checks:
            extra_list = getattr(report, 'extras', [])
            
            for check in vision_tester.checks:
                # Read screenshot and convert to base64
                screenshot_path = check['screenshot_path']
                if os.path.exists(screenshot_path):
                    with open(screenshot_path, 'rb') as f:
                        screenshot_b64 = base64.b64encode(f.read()).decode('utf-8')
                    
                    # Add HTML section for this check
                    html = f'''
                    <div style="border: 1px solid #ddd; margin: 10px 0; padding: 10px; border-radius: 5px; background-color: #f9f9f9;">
                        <h4 style="color: {'green' if check['passed'] else 'red'}; margin-top: 0;">
                            {'✅ PASSED' if check['passed'] else '❌ FAILED'}: {check['prompt']}
                        </h4>
                        <p><strong>URL:</strong> <code>{check['url']}</code></p>
                        <p><strong>AI Response:</strong> {check['ai_response']}</p>
                        <details style="margin-top: 10px;">
                            <summary style="cursor: pointer; font-weight: bold;">📸 View Screenshot</summary>
                            <img src="data:image/png;base64,{screenshot_b64}" style="max-width: 100%; border: 1px solid #ccc; margin-top: 10px; border-radius: 3px;" />
                        </details>
                    </div>
                    '''
                    extra_list.append(extras.html(html))
            
            report.extras = extra_list

def pytest_html_report_title(report):
    """Customize the HTML report title."""
    report.title = "Semantic Vision Test Report"
