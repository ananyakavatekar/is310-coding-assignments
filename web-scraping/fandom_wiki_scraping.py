import csv
import json
import time

import cloudscraper
from bs4 import BeautifulSoup

URL = "https://cookieclicker.wiki.gg/wiki/Achievements"
CSV_FILE = "cookie_clicker_achievements.csv"
JSON_FILE = "cookie_clicker_achievements.json"


def make_scraper():
    return cloudscraper.create_scraper()


def get_html(scraper, url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://cookieclicker.wiki.gg/",
    }

    response = scraper.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    time.sleep(1)
    return response.text


def clean_text(text):
    return " ".join(text.split()).strip()


def parse_achievements(html):
    soup = BeautifulSoup(html, "html.parser")
    records = []

    tables = soup.find_all("table")

    for table in tables:
        rows = table.find_all("tr")
        if len(rows) < 2:
            continue

        # get first row text to identify achievement tables
        first_row_cells = rows[0].find_all(["th", "td"])
        first_row_text = " ".join(clean_text(cell.get_text(" ", strip=True)) for cell in first_row_cells)

        # keep only tables that look like achievement tables
        if "Icon" not in first_row_text or "Name" not in first_row_text or "Description" not in first_row_text or "ID" not in first_row_text:
            continue

        # category is usually the first meaningful word(s) before "Icon Name Description ID"
        category = first_row_text.replace("Icon Name Description ID", "").strip()

        for row in rows[1:]:
            cells = row.find_all("td")
            if len(cells) < 4:
                continue

            # typical structure: icon | name | description | id
            name = clean_text(cells[1].get_text(" ", strip=True))
            description = clean_text(cells[2].get_text(" ", strip=True))
            achievement_id = clean_text(cells[3].get_text(" ", strip=True))

            if not name:
                continue

            records.append(
                {
                    "category": category,
                    "name": name,
                    "description": description,
                    "id": achievement_id,
                    "source_page": URL,
                }
            )

    return records


def save_csv(data, filename):
    if not data:
        return

    fieldnames = list(data[0].keys())
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def save_json(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def main():
    scraper = make_scraper()

    print("Getting achievements page...")
    html = get_html(scraper, URL)

    print("Parsing achievements...")
    records = parse_achievements(html)

    print(f"Found {len(records)} achievements.")

    save_csv(records, CSV_FILE)
    save_json(records, JSON_FILE)

    print(f"Saved to {CSV_FILE} and {JSON_FILE}")


if __name__ == "__main__":
    main()