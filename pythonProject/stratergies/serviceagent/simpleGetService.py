import time
from urllib.request import urlopen

import requests as r
import ssl
import certifi


headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Host': 'etmarketsapis.indiatimes.com',
    'Origin': 'https://economictimes.indiatimes.com',
    'Referer': 'https://economictimes.indiatimes.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.110 Safari/537.36 '
}


def make_cookies(cookie_dict: dict) -> str:
    return "; ".join(f"{k}={v}" for k, v in cookie_dict.items())


def get_endpoint_data(api_endpoint: str) -> str:
    with r.Session() as connection:
        retry = 0
        while retry != 10:
            try:
                the_real_slim_shady = connection.get(f"{api_endpoint}", timeout=20, verify=False)
                if the_real_slim_shady == '':
                    retry = retry + 1
                    time.sleep(5)
                    continue
                else:
                    return the_real_slim_shady.json()
                    # break
            except ConnectionError as err:
                retry = retry + 1
                time.sleep(5)
                print(err)