import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

LOC_SEARCH_URL = "https://www.loc.gov/search/"
EUROPEANA_SEARCH_URL = "https://api.europeana.eu/record/v2/search.json"
OUTPUT_FILE = Path("loc_api_culture_data.json")


def get_loc_item():
    params = {
        "q": "women suffrage protest","q": "women suffrage protest",
        "fo": "json",
        "c": 1,
    }

    response = requests.get(LOC_SEARCH_URL, params=params, timeout=30)
    response.raise_for_status()
    loc_data = response.json()

    print("\n=== LIBRARY OF CONGRESS API RESPONSE ===")
    print(json.dumps(loc_data, indent=2, ensure_ascii=False))

    results = loc_data.get("results", [])
    if not results:
        raise ValueError("No results found from the Library of Congress API.")

    item = results[0]

    cleaned_loc_item = {
        "title": item.get("title"),
        "date": item.get("date"),
        "description": item.get("description"),
        "subject": item.get("subject"),
        "item_type": item.get("type"),
        "image_url": item.get("image_url"),
        "url": item.get("url"),
    }

    return cleaned_loc_item


def search_europeana(query, api_key):
    params = {
        "wskey": api_key,
        "query": query,
        "rows": 1,
        "media": "true",
    }

    response = requests.get(EUROPEANA_SEARCH_URL, params=params, timeout=30)
    response.raise_for_status()
    europeana_data = response.json()

    items = europeana_data.get("items", [])
    if not items:
        return None

    item = items[0]

    print(f"\n=== EUROPEANA ITEM RESPONSE FOR QUERY: {query} ===")
    print(json.dumps(item, indent=2, ensure_ascii=False))

    cleaned_europeana_item = {
        "id": item.get("id"),
        "title": item.get("title"),
        "type": item.get("type"),
        "dataProvider": item.get("dataProvider"),
        "provider": item.get("provider"),
        "country": item.get("country"),
        "guid": item.get("guid"),
        "link": item.get("link"),
        "edmPreview": item.get("edmPreview"),
    }

    return cleaned_europeana_item


def main():
    load_dotenv()
    api_key = os.getenv("EUROPEANA_API_KEY")

    if not api_key:
        raise ValueError("Missing EUROPEANA_API_KEY in .env")

    loc_item = get_loc_item()

    queries = [
    loc_item["title"],
    "women suffrage protest",
    ]

    europeana_item = None
    for query in queries:
        if query:
            europeana_item = search_europeana(query, api_key)
            if europeana_item is not None:
                break

    if europeana_item is None:
        raise ValueError("No related Europeana item was found.")

    final_data = {
        "selected_api": "Library of Congress API",
        "loc_item": loc_item,
        "europeana_item": europeana_item,
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(final_data, f, indent=2, ensure_ascii=False)

    print(f"\nSaved cleaned item data to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
