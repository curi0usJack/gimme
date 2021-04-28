import requests
import subprocess
import datetime
import json
import random
from pushover import Client


def sendpush(message):
    apikey = "<your key>"
    userkey = "<user key>"
    # client = Client(userkey, api_token=apikey)
    # client.send_message(message)
    print(message)


def search(url, searchstring, negativesearch):
    ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15"
    headers = { 'User-Agent': ua
                # 'Set-Cookie': "SID=81f6103a-b720-4e03-aa59-6bfece800c84; path=/; domain=.bestbuy.com",
                # 'Set-Cookie': "bby_cbc_lb=p-browse-e; expires=Wed, 28-Apr-2021 00:54:38 GMT; path=/; domain=.bestbuy.com",
                # 'x-employment': "If you are reading this, consider a job at BestBuy.com http://www.bestbuy-jobs.com/job-family/all-corporate-careers/"
            }
    resp = requests.get(url, headers=headers)
    content = str(resp.content)
    # do some stuff
    if resp.status_code == 200:
        found = False
        if negativesearch:
            if not searchstring in content:
                found = True
        else:
            if searchstring in content:
                found = True

        if found:
            if hour > 5 and hour < 11:
                sendpush("PS5 Found: {}".format(url))
    else:
        sendpush("Error connecting to PS5 site: {}".format(url))

hour = datetime.datetime.now().hour

# First URL
url = "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"
search(url, "Sold Out</button>", True)

# For subsequent runs, add more urls and calls to search()
# url = "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"
# search(url, "Sold Out</button>", True)



