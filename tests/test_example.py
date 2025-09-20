# tests/test_example.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import shutil
import pytest

def test_example_dot_com():
    print("👉 Entered test_example_dot_com")  # marker for program start

    # -------------------------
    # Chrome options for headless Linux
    # -------------------------
    options = Options()
    options.add_argument("--headless=new")  # or "--headless=chrome"
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--window-size=1920,1080")

    # -------------------------
    # Detect Chromium binary
    # -------------------------
    chromium_path = shutil.which("chromium") or shutil.which("chromium-browser")
    if not chromium_path:
        raise RuntimeError("No Chromium or Chrome binary found. Run: sudo apt install chromium")
    options.binary_location = chromium_path
    print(f"Using browser binary: {chromium_path}")

    # -------------------------
    # Fetch matching ChromeDriver for Chromium
    # -------------------------
    service = Service(ChromeDriverManager(chrome_type="chromium").install())

    # -------------------------
    # Launch browser and visit page
    # -------------------------
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://example.com")

    # Simple assertion
    assert "Example Domain" in driver.title
    print(f"Page title: {driver.title}")

    driver.quit()
