from playwright.sync_api import sync_playwright
import re

urls = [
    "https://sanand0.github.io/tdsdata/seed0.html",
    "https://sanand0.github.io/tdsdata/seed1.html",
    "https://sanand0.github.io/tdsdata/seed2.html",
    "https://sanand0.github.io/tdsdata/seed3.html",
    "https://sanand0.github.io/tdsdata/seed4.html",
    "https://sanand0.github.io/tdsdata/seed5.html",
    "https://sanand0.github.io/tdsdata/seed6.html",
    "https://sanand0.github.io/tdsdata/seed7.html",
    "https://sanand0.github.io/tdsdata/seed8.html",
    "https://sanand0.github.io/tdsdata/seed9.html",
]

total = 0

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    for url in urls:
        page.goto(url)
        page.wait_for_load_state("networkidle")

        # get ALL visible text inside tables
        table_text = page.inner_text("table")

        # extract all numbers (ints + decimals)
        numbers = re.findall(r"-?\d+\.?\d*", table_text)

        for n in numbers:
            total += float(n)

    browser.close()

print(f"TOTAL_SUM={total}")
