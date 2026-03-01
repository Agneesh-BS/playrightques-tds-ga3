from playwright.sync_api import sync_playwright
import re

seeds = range(10)
total_sum = 0

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    for seed in seeds:
        url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
        page.goto(url)

        # wait for tables to load
        page.wait_for_selector("table")

        # get all text from tables
        tables_text = page.inner_text("body")

        # extract numbers
        nums = re.findall(r"-?\d+", tables_text)
        nums = [int(n) for n in nums]

        total_sum += sum(nums)

    browser.close()
print("24f1001207@ds.study.iitm.ac.in")
print(f"TOTAL SUM: {total_sum}")
