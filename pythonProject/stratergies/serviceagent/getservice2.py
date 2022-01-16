import time

import requests

headers = {
    'Host': 'www.nseindia.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}


def make_cookies(cookie_dict: dict) -> str:
    return "; ".join(f"{k}={v}" for k, v in cookie_dict.items())


def get_endpoint_data(api_endpoint: str) -> str:
    with requests.Session() as connection:
        try:
            authority = connection.get("https://www.nseindia.com", headers=headers, timeout=30)
            historical_json = connection.get(api_endpoint, headers=headers)
            bm_sv_string = make_cookies(historical_json.cookies.get_dict())
            cookies = make_cookies(authority.cookies.get_dict()) + bm_sv_string
            connection.headers.update({**headers, **{"cookie": cookies}})

            the_real_slim_shady = connection.get(f"{api_endpoint}")
            return the_real_slim_shady.json()
        except requests.exceptions.Timeout as err:
            print(err)