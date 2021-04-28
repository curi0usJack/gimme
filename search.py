import requests
import subprocess
import datetime
import json
import random
from pushover import Client


def search(url, searchstring):
    ua = "Safari: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15"
    headers = { 'User-Agent': ua }
    resp = requests.get(url, headers=headers)
    print(resp.status_code)


url = "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p\\?skuId\\=6426149"
search(url)
