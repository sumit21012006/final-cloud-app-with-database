import os
import shutil
from playwright.sync_api import sync_playwright

output_dirs = [
    r"e:\College\Coursera",
    r"e:\College\Coursera\final-cloud-app-with-database"
]

def capture_screenshots():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 800}, device_scale_factor=2)

        # ---------------------------------------------------------
        # SCREENSHOT 1: 03-admin-site
        # ---------------------------------------------------------
        print("Navigating to Django admin login...")
        page.goto("http://127.0.0.1:8000/admin/login/?next=/admin/")
        page.fill('input[name="username"]', 'admin')
        page.fill('input[name="password"]', 'admin123')
        page.click('input[type="submit"]')
        page.wait_for_timeout(1000)

        for d in output_dirs:
            png_path = os.path.join(d, "03-admin-site.png")
            page.screenshot(path=png_path)
            # also create copy without extension
            no_ext_path = os.path.join(d, "03-admin-site")
            shutil.copyfile(png_path, no_ext_path)
        print("Captured: 03-admin-site.png")

        # ---------------------------------------------------------
        # SCREENSHOT 2: 07-final
        # ---------------------------------------------------------
        print("Navigating to user login...")
        page.goto("http://127.0.0.1:8000/onlinecourse/login/")
        page.fill('input[name="username"]', 'sumit')
        page.fill('input[name="psw"]', 'student123')
        page.click('button[type="submit"]')
        page.wait_for_timeout(1000)

        print("Navigating to exam result...")
        page.goto("http://127.0.0.1:8000/onlinecourse/course/1/submission/1/result/")
        page.wait_for_timeout(1000)

        for d in output_dirs:
            png_path = os.path.join(d, "07-final.png")
            page.screenshot(path=png_path)
            # also create copy without extension
            no_ext_path = os.path.join(d, "07-final")
            shutil.copyfile(png_path, no_ext_path)
        print("Captured: 07-final.png")

        browser.close()

if __name__ == "__main__":
    capture_screenshots()
