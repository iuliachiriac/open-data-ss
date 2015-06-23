#!/usr/bin/env python3
import sys
import requests
from bs4 import BeautifulSoup
import json


def main():
    resp = requests.get("http://www.hotnews.ro")

    if not resp.status_code == 200:
        print('Request failed wih code {}'.format(resp.status_code))
        sys.exit(1)

    soup = BeautifulSoup(resp.text)
    articles = soup.find_all('div', class_='articol_lead_full')

    all_categories = {}
    for article in articles:
        category_text = article.find('span', class_='categoria').a.text
        categories = [c.strip() for c in category_text.split('|')]
        for category in categories:
            if category in all_categories:
                all_categories[category] += 1
            else:
                all_categories[category] = 1

    print(json.dumps(all_categories, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    main()
