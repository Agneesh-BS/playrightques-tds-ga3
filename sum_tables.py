from playwright.sync_api import sync_playwright

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
        cells = page.query_selector_all("table td")
        for c in cells:
            text = c.inner_text().strip()
            if text.replace(".", "", 1).isdigit():
                total += float(text)

    browser.close()

print(f"TOTAL_SUM={total}")
