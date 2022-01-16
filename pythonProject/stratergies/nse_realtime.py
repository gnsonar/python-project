from dtos.Equity import Equity
from serviceagent import getservice as service
from utils import emailUtils, utils
import json
import time

api_endpoint = "https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O"


def execute_nse_scanner():
    retry = 0
    output = ''
    while retry != 10:
        output = service.get_endpoint_data(api_endpoint, 'maxpain.txt')
        if output == '':
            retry = retry + 1
            time.sleep(10)
            continue
        else:
            break
    buys = []
    sells = []

    if output != '':
        data = json.loads(output)
        for record in data['data']:
            if not record['open'].__contains__('.') and \
                    not record['dayLow'].__contains__('.') and \
                    record['dayLow'].__eq__(record['open']):
                buy = Equity(record['symbol'], record['open'], '', record['dayLow'])
                buys.append(buy)

        for record in data['data']:
            if not record['open'].__contains__('.') and \
                    not record['dayHigh'].__contains__('.') and \
                    record['dayHigh'].__eq__(record['open']):
                sell = Equity(record['symbol'], record['open'], record['dayHigh'], '')
                sells.append(sell)

        text = ''
        if len(buys) > 0:
            text = text + '<b>buy positions</b><br/>'
            for e in buys:
                text = text + e.code + ' ' + e.open + ' ' + e.low + '<br/>'
        text = text + '<br/>'
        if len(sells) > 0:
            text = text + '<b>sell positions</b><br/>'
            for e in sells:
                text = text + e.code + ' ' + e.open + ' ' + e.high + '<br/>'
        senders = ["gautam.sonar89@gmail.com", "khushalnso@gmail.com"]
        subject = "Dot Zero Zero Positions " + utils.current_ist_time()
        html = """\
        <html>
          <head></head>
          <body>
            <p> """ + text + """
            </p>
          </body>
        </html>
        """
        emailUtils.send_email(subject, html, senders)

