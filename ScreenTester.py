from trendtemplatetest import TrendTemplateTest;

# Creates Price Column for each ticker (method from TrendTemplateTest file) and runs tests.
def getTestResult(name):
    t = TrendTemplateTest(name);
    t.createPriceColumn();
    result = t.runTest();
    if(result):
        printedString = "PASS"
    else:
        printedString = "FAIL"
    return result

# Prints test result for each ticker to terminal screen.
def printResults(name, printedString):
    print(name, "    ", printedString)

# Writes test results to log file for caching.
def writeResults(name, printedString):
    r = open("StocksthatPassedScreen.txt", "a")
    r.write(str(name) + "    " + str(printedString) + "    \n")
    r.close();
