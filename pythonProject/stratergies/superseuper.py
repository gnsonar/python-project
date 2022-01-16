import json
import secrets
import string
import time

from serviceagent import getservice as service
from utils import emailUtils, utils

sectors = ['NIFTY%20AUTO',
           'NIFTY%20BANK',
           'NIFTY%20ENERGY',
           'NIFTY%20FINANCIAL%20SERVICES',
           'NIFTY%20FINANCIAL%20SERVICES%2025/50',
           'NIFTY%20FMCG',
           'NIFTY%20IT',
           'NIFTY%20MEDIA',
           'NIFTY%20METAL',
           'NIFTY%20PHARMA',
           'NIFTY%20PSU%20BANK',
           'NIFTY%20REALTY',
           'NIFTY%20PRIVATE%20BANK',
           'NIFTY%20HEALTHCARE%20INDEX',
           'NIFTY%20CONSUMER%20DURABLES',
           'NIFTY%20OIL%20%26%20GAS']
nse_end_point = 'https://www.nseindia.com/api/equity-stockIndices?index='


def sortSecond(val):
    return val['change']


def top_stocks(sector: str, data, gainer):
    top_stocks = []
    for stock in data:
        if stock['symbol'] != sector and \
                ((gainer and stock['pChange'] > 0) or (not gainer and stock['pChange'] < 0)):
            stock_data = {'symbol': stock['symbol'],
                          'identifier': stock['identifier'],
                          'lastPrice': stock['lastPrice'],
                          'change': stock['pChange']}
            top_stocks.append(stock_data)
            if gainer:
                top_stocks.sort(key=sortSecond, reverse=True)
            else:
                top_stocks.sort(key=sortSecond, reverse=False)
            if len(top_stocks) > 3:
                top_stocks = top_stocks[0:3]
    return top_stocks


def call_super_se_uper():
    gainers_sectors = []
    losers_sectors = []
    for sector in sectors:
        res = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(10))
        res = res + '.txt'
        retry = 0
        while retry != 6:
            data = service.get_endpoint_data(api_endpoint=nse_end_point + sector, file=res)
            if data == '':
                retry = retry + 1
                time.sleep(2)
                continue
            else:
                break

        if data != '':
            output = json.loads(data)
            sector_data = {'sector': output['metadata']['indexName'],
                           'change': output['metadata']['percChange']}
            if sector_data['change'] > 0:
                sector_data['stocks'] = top_stocks(sector, output['data'], True)
                gainers_sectors.append(sector_data)
            else:
                sector_data['stocks'] = top_stocks(sector, output['data'], False)
                losers_sectors.append(sector_data)

    gainers_sectors.sort(key=sortSecond, reverse=True)
    losers_sectors.sort(key=sortSecond, reverse=False)
    if len(gainers_sectors) > 3:
        gainers_sectors = gainers_sectors[0:3]
    if len(losers_sectors) > 3:
        losers_sectors = losers_sectors[0:3]

    senders = ["gautam.sonar89@gmail.com", "khushalnso@gmail.com"]
    create_body_send_emails(gainers_sectors, losers_sectors, senders)


def create_body_send_emails(gainers_sectors, losers_sectors, senders):
    text = ''
    if len(gainers_sectors) > 0:
        text = text + '<p><span style="color: #99cc00;"><strong>Buy Positions</strong></span></p> '
        for s in gainers_sectors:
            text = text + '<table style="border-collapse: collapse; width: 100%; height: 18px;" border="1">' \
                          '<tbody>' \
                          '<tr style="height: 18px;">' \
                          '<td style="width: 23.4024%; height: 18px;">Sector: <strong> ' + s[
                       'sector'] + '</strong></td>' \
                                   '<td style="width: 38.2988%; height: 18px;">Change : <span style="color: ' \
                                   '#99cc00;"><strong>' + s['change'].__str__() + '%</strong></span></td>' \
                                                                                  '</tr>' \
                                                                                  '</tbody>' \
                                                                                  '</table>' \
                                                                                  '<table style="border-collapse: collapse; width: 100%; height: 36px;" border="1">' \
                                                                                  '<tbody>' \
                                                                                  '<tr style="height: 18px;">' \
                                                                                  '<td style="width: 25%; text-align: center; height: 18px;"><strong>Stock</strong></td>' \
                                                                                  '<td style="width: 24.1364%; text-align: center; height: 18px;"><strong>Identifier</strong></td>' \
                                                                                  '<td style="width: 25.8636%; text-align: center; height: 18px;"><strong>Last Price</strong></td>' \
                                                                                  '<td style="width: 25%; text-align: center; height: 18px;"><strong>Change</strong></td>' \
                                                                                  '</tr>'
            for s1 in s['stocks']:
                text = text + '<tr style="height: 18px;">' \
                              '<td style="width: 25%; text-align: center; height: 18px;">' + s1['symbol'] + '</td>' \
                                                                                                            '<td style="width: 24.1364%; text-align: center; height: 18px;">' + \
                       s1['identifier'] + '</td>' \
                                          '<td style="width: 25.8636%; text-align: center; height: 18px;">' + s1[
                           'lastPrice'].__str__() + '</td>' \
                                                    '<td style="width: 25%; text-align: center; height: 18px;"><span style="color: #99cc00;">' + \
                       s1['change'].__str__() + '</span></td>' \
                                                '</tr>'
            text = text + '</tbody></table><br/>'

    if len(losers_sectors) > 0:
        text = text + '<p><span style="color: #ff0000;"><strong>Sell Positions</strong></span></p> '
        for s in losers_sectors:
            text = text + '<table style="border-collapse: collapse; width: 100%; height: 18px;" border="1">' \
                          '<tbody>' \
                          '<tr style="height: 18px;">' \
                          '<td style="width: 23.4024%; height: 18px;">Sector: <strong> ' + s[
                       'sector'] + '</strong></td>' \
                                   '<td style="width: 38.2988%; height: 18px;">Change : <span style="color: ' \
                                   '#ff0000;"><strong>' + s['change'].__str__() + '%</strong></span></td>' \
                                                                                  '</tr>' \
                                                                                  '</tbody>' \
                                                                                  '</table>' \
                                                                                  '<table style="border-collapse: collapse; width: 100%; height: 36px;" border="1">' \
                                                                                  '<tbody>' \
                                                                                  '<tr style="height: 18px;">' \
                                                                                  '<td style="width: 25%; text-align: center; height: 18px;"><strong>Stock</strong></td>' \
                                                                                  '<td style="width: 24.1364%; text-align: center; height: 18px;"><strong>Identifier</strong></td>' \
                                                                                  '<td style="width: 25.8636%; text-align: center; height: 18px;"><strong>Last Price</strong></td>' \
                                                                                  '<td style="width: 25%; text-align: center; height: 18px;"><strong>Change</strong></td>' \
                                                                                  '</tr>'
            for s1 in s['stocks']:
                text = text + '<tr style="height: 18px;">' \
                              '<td style="width: 25%; text-align: center; height: 18px;">' + s1['symbol'] + '</td>' \
                                                                                                            '<td style="width: 24.1364%; text-align: center; height: 18px;">' + \
                       s1['identifier'] + '</td>' \
                                          '<td style="width: 25.8636%; text-align: center; height: 18px;">' + s1[
                           'lastPrice'].__str__() + '</td>' \
                                                    '<td style="width: 25%; text-align: center; height: 18px;"><span style="color: #ff0000;">' + \
                       s1['change'].__str__() + '</span></td>' \
                                                '</tr>'
            text = text + '</tbody></table><br/>'

    subject = "Super Se Upar Positions " + utils.current_ist_time()
    html = """\
    <html>
      <head></head>
      <body>
        """ + text + """
      </body>
    </html>
    """
    emailUtils.send_email(subject, html, senders)
