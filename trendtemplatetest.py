from fixedlist import fixedlist;
import statistics as st;
import csv;
import pandas as pd;
from Tests import Tests;
class TrendTemplateTest:
    # The strength parameter determines how strict the Two Hundred Day MA Trending Up Test will be tested. 1 is minimum strength (looking for 1 month up trend), 5 is maximum strength (5 month up trend),
    #   although higher numbers (up to 19 (400 data points for each price list)) can be used. Using higher numbers may be used to screen for higher performing stocks with
    #   (potentially) good fundamentals that cause their longer than usual uptrends. The strength parameter is optional.
    def __init__(self, name, strength=None):
        self.name = name;
        self.strength = strength if strength is not None else 1;
        self.result = False;
        self.mact = None;
        self.ptmact = None;
        self.pthlct = None;
        self.thdmatut = None;
        self.fullcsvname= None;
        self.colcsvname = None;

    # This method creates a new file for each AlphaVantage file. This new file only contains the prices column from each AlphaVantage file.
    def createPriceColumn(self):
        self.fullcsvname = "daily_" + self.name + ".csv"
        self.colcsvname = "daily_" + self.name + "_close.csv"
        my_csv = pd.read_csv(self.fullcsvname)
        column = my_csv.close
        column.to_csv(self.colcsvname, index=False, header=False, line_terminator = " ")

    # This method tests each price series against the tests written in the "Tests" class file. More information in the comment within the method.
    def runTest(self):
        prices = []
        f = open(self.colcsvname, "r")
        for i in f:
            for l in i.split():
                prices.append(float(l))
        prices = prices[0:401]
        prices = prices[::-1]
        twohundredday = fixedlist(200);
        onefiftyday = fixedlist(150);
        fiftyday = fixedlist(50);
        thdmalist = [];
        ofdmalist = [];
        fdmalist = [];
        count = 0;
        # The below creates a fixedlist for the series' 200 Day-, 150 Day-, and 50 Day- moving averages, and sends them to the Tests class file to run each of the tests listed there.
        # If each sub series passes the test in that file, this  method returns true.
        for i in prices:
            current = round(i, 2);
            twohundredday.append(current)
            onefiftyday.append(current)
            fiftyday.append(current)
            if(count >= 50):
                fdmalist.append(round(st.mean(fiftyday), 2))
            if(count >= 150):
                ofdmalist.append(round(st.mean(onefiftyday), 2))
            if(count >= 200):
                thdmalist.append(round(st.mean(twohundredday), 2))
            count += 1;
        if(len(thdmalist) == 0):
            return False;
        T = Tests(thdmalist, ofdmalist, fdmalist, prices);
        self.mact = T.MAComparisonTest();
        self.ptmact = T.PriceToMAComparisonTest();
        self.pthlct = T.PriceToHighLowComparisonTest();
        self.thdmatut = T.THDMATrendingUpTest(self.strength);

        if(self.mact and self.ptmact and self.pthlct and self.thdmatut):
            self.result = True;
        return self.result;
    # This method prints the results for each ticker price series to the terminal.
    def printResults(self):
        print("Result of full screen: ", self.result);
        print("Individual Tests: ");
        print("Result of Moving Averages Comparison Test: ", self.mact);
        print("Result of Price to Moving Averages Comparison Test: ", self.ptmact);
        print("Result of Price To 52 Week High and Low Comparison Test: ", self.pthlct);
        print("Result of Two Hundred Day Moving Average Trending Up Test: ", self.thdmatut);
