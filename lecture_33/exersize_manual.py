import time

import requests
from bs4 import BeautifulSoup

titles = []


def get_title(specific_url):
    try:
        resp = requests.get(specific_url)
        if resp.status_code != 200:
            return None, f"Incorrect status_code {resp.status_code} for {specific_url}"
    except Exception as err:
        return None, f"Error: {err} for {specific_url}"

    soup = BeautifulSoup(resp.content, "html.parser")
    err = None
    try:
        title = soup.title.string
    except Exception as e:
        title = None
        err = e

    return title, err


def main(specific_url):
    global titles

    title, err = get_title(specific_url)
    titles.append(
        {
            "url": specific_url,
            "title": title,
            "err": err,
        }
    )


if __name__ == "__main__":
    # Fetch the urls from a file
    # urls = get_urls()
    start_time = time.perf_counter()

    for url in urls:
        main(url)

    end_time = time.perf_counter()

    print(titles)
    print(f"Total time: {end_time - start_time}")
