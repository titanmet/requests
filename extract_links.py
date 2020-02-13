import requests
import re


def extract_links(url):
    r = requests.get(url)
    links = re.findall(r'href="(.*?)"', r.text, flags=re.IGNORECASE)
    return links

# print(extract_links('https://habrahabr.ru/'))
# print(extract_links('http://www.moscowpython.ru/meetup/46/'))