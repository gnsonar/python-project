class Equity:
    code: any
    open: any
    high: any
    low: any

    def __init__(self, code, open, high, low):
        self.code = code
        self.open = open
        self.high = high
        self.low = low

    def getcode(self) -> any:
        return self.code

    def getopen(self) -> any:
        return self.open

    def gethigh(self) -> any:
        return self.high

    def getlow(self) -> any:
        return self.low

    def tostr(self):
        print('code:' + self.code + ' open:' + self.open + ' high:' + self.high + ' low:' + self.low)
