

from serviceagent import simpleGetService as service
import superseuper

et_end_point = 'https://etmarketsapis.indiatimes.com/ET_Stats/getAllIndices?pagesize=100&exchange=nse&sortby=value' \
               '&sortorder=desc&marketcap='

stocks_end_point = 'https://etmarketsapis.indiatimes.com/ET_Stats/getIndexByIds?pagesize=25&exchange=NSE&sortby' \
                   '=percentChange&sortorder=desc&indexid={}&company=true&marketcap=&indexname={}'


def sortSecond(val):
    return val['change']


def top_stocks(sector, gainer):
    stocks = []
    url = stocks_end_point.format(sector['indexId'], sector['sector'].replace(" ", "%20"))
    stockData = service.get_endpoint_data(url)
    for stock in stockData['searchresult'][0]['companies']:
        if stock['current'] < 500 and \
                ((gainer and stock['percentChange'] > 0) or (not gainer and stock['percentChange'] < 0)):
            stock_data = {'symbol': stock['symbol'],
                          'identifier': stock['companyName'],
                          'lastPrice': stock['current'],
                          'change': stock['percentChange']}
            stocks.append(stock_data)
    if gainer:
        stocks.sort(key=sortSecond, reverse=True)
    else:
        stocks.sort(key=sortSecond, reverse=False)
    if len(stocks) > 4:
        stocks = stocks[0:4]
    return stocks


def call_super_se_uper():
    gainers_sectors = []
    losers_sectors = []
    data = service.get_endpoint_data(et_end_point)
    if data != '':
        for sector in data['searchresult']:
            sector_data = {'sector': sector['indexName'],
                           'change': sector['perChange'], 'indexId': sector['indexId']}
            if sector_data['change'] > 0:
                gainers_sectors.append(sector_data)
            else:
                losers_sectors.append(sector_data)

        gainers_sectors.sort(key=sortSecond, reverse=True)
        losers_sectors.sort(key=sortSecond, reverse=False)

        if len(gainers_sectors) > 3:
            gainers_sectors = gainers_sectors[0:3]
        if len(losers_sectors) > 3:
            losers_sectors = losers_sectors[0:3]

        for s in gainers_sectors:
            s['stocks'] = top_stocks(s, True)
        for s in losers_sectors:
            s['stocks'] = top_stocks(s, False)

        senders = ["gautam.sonar89@gmail.com", "khushalnso@gmail.com"]
        superseuper.create_body_send_emails(gainers_sectors, losers_sectors, senders)