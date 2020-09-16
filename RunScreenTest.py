from fixedlist import fixedlist;
import statistics as st;
import csv;
from Tests import Tests;
from trendtemplatetest import TrendTemplateTest;
import time;
import os.path
from os import path
from ScreenTester import getTestResult;
from ScreenTester import printResults;
from ScreenTester import writeResults;

# The below prints results of the screener test for each of the stocks in your "stock-names.txt" list.
printedString = None;
result = None;
f = open("stock-names.txt", "r")
notinlist = 0;
for i in f:
    #if there is an unusual number of path errors, the below stops the program so you can inspect if you have all of the files you are trying to analyze.
    if(notinlist > 100):
        break;
    name = i;
    name = name.rstrip('\n')
    filename = "daily_" + name + ".csv"
    if(path.exists(filename)):
        res = getTestResult(name);
        printResults(name, res);
        writeResults(name, res);
    else:
        print(name + "     File Not Found")
        notinlist += 1;
