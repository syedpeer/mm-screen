# MAComparisonTest means testing Fifty Day MA > One Fifty Day MA > Two Hundred Day MA
class Tests:
    def __init__(self, thdmalist, ofdmalist, fdmalist, prices):
        self.thdmalist = thdmalist;
        self.ofdmalist = ofdmalist;
        self.fdmalist = fdmalist;
        self.prices = prices;
        #The below get the latest numbers
        self.thd = self.thdmalist[len(self.thdmalist)-1]
        self.ofd = self.ofdmalist[len(self.ofdmalist)-1]
        self.fd = self.fdmalist[len(self.fdmalist)-1]
        self.latestPrice = prices[len(prices)-1]
        self.last52wksprices = prices[len(prices)-253:len(prices)]
        self.fiftytwowkhigh = max(self.last52wksprices);
        self.fiftytwowklow = min(self.last52wksprices);

    # MAComparisonTest (Moving Average Comparison Test) tests  Fifty Day Moving Average > One Fifty Day Moving Average > Two Hundred Day Moving Average -> returns boolean
    def MAComparisonTest(self):
          result = False;
          if(self.thd < self.ofd and self.ofd < self.fd):
              result = True;
          return result;

    # This method test to see if the latest price exceeds the 200 day moving average, the 150 day moving average, and the fifty day moving average. Returns boolean.
    def PriceToMAComparisonTest(self):
        result = False;
        if(self.latestPrice > self.thd and self.latestPrice > self.ofd and self.latestPrice > self.fd):
            result = True;
        return result;

    # This method tests to see if the current price is greater than 1.3 times the 52-week low and greater than .75 times the 52-week high.
    def PriceToHighLowComparisonTest(self):
        result = False;
        lowTarget = 1.3*self.fiftytwowklow;
        highTarget = .75*self.fiftytwowkhigh;
        if(self.latestPrice >= lowTarget and self.latestPrice >= highTarget):
            result = True;
        return result;

    # Note: There are an average of 21 trading days in a month and an average of 21*x trading days in x months.
    # This method tests to see if the series' 200-Day Moving Average has been trending up for 21*number of months (trading days in x months). Returns boolean
    def THDMATrendingUpTest(self, numMonths: int):
        limit = 21*numMonths;
        testthdmalist = self.thdmalist[len(self.thdmalist)-limit : len(self.thdmalist)];
        result = True;
        previous = -1;
        for i in testthdmalist:
            if i <= previous:
                return False;
            previous = i;
        return result;
