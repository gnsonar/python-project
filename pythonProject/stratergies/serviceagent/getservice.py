import subprocess
import os


def get_endpoint_data(api_endpoint: str, file: str) -> str:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    if not os.path.exists(file):
        open(file, 'x').close()
    subprocess.Popen('curl "' + api_endpoint + '" -H '
                     '"authority: '
                     'beta.nseindia.com" -H "cache-control: max-age=0" -H "dnt: 1" -H "upgrade-insecure-requests: 1" '
                     '-H '
                     '"user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/79.0.3945.117 Safari/537.36" -H "sec-fetch-user: ?1" -H "accept: text/html,'
                     'application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                     'application/signed-exchange;v=b3;q=0.9" -H "sec-fetch-site: none" -H "sec-fetch-mode: navigate" '
                     '-H '
                     '"accept-encoding: gzip, deflate, br" -H "accept-language: en-US,en;q=0.9,hi;q=0.8" --compressed '
                     ' -o '
                     '' + file, shell=True)

    f = open(file, "r")
    var = f.read()
    return '' if var.__contains__('Resource not found') else var
