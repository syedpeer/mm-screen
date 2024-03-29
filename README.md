
# mm-screen

###### Credits:

Stock screener described in the book "Trade Like a Stock Market Wizard" by Mark Minervini, to be used for identifying superperformance stocks.


As a critical first note, all credit for the development of the screener is to be given to Mark Minervini. You can read an in-depth description of the screener and much more important and useful content in his book, link [here](https://www.amazon.com/Trade-Like-Stock-Market-Wizard/dp/0071807225).

Credit is also due to AlphaVantage, a ticker data company that supplies comprehensive, csv-formatted, historical price data. This is a great free resource. Link [here](https://www.alphavantage.co/).

Finally, the very useful [Selenium](https://www.selenium.dev/) project must be credited as well. 


###### How to Use:

1. Download database of historical prices by running the "av-bot.py" file. By default, this will download prices for all companies listed in the stock-names.txt file, listing all companies in the NASDAQ. Adjust this file if you need a smaller subset of these tickers. More information below.

2. Run the test by typing into terminal "python RunScreenTest.py" in the same directory as the rest of the files downloaded here and your csv price database.


###### Desciption of the screener:

In short, Minervini states in his book that superperformance stocks, stocks that are set to give investors unusally high returns can often be detected by using a specific screen. 

  1. The fifty-day moving average for the ticker must exceed the 150-day moving average, which must exceed the 200-day moving average. (50DMA > 150DMA > 200DMA)
  2. The current price of the underlying must exceed the fifty-day moving average, the 150-day moving average, and the 200-day moving average. (Current Price > 50DMA and Current Price > 150DMA and Current Price > 200DMA)
  3. The current price of the stock must be greater than 1.3 times the fifty-two-week low of the stock price and greater than 0.75 times the fifty-two-week high. [(Current Price > 1.3 * 52WLow) and (Current Price > 0.75 * 52WHigh)]
  4. The 200-day moving average has been trending upward for X months. You choose the X (the default value is X=1 and can be modified in the trendtemplatetest.py file). 
      (200DMA trending up for at least 1 month)
      
###### Results of the screener:

The first screen on the NASDAQ was performed on April 17th, 2020. Using August 17th as a benchmark, the mean return over this four month period was +31.17%, with the median return being +11.37%. You can look at the set of statistics [here](https://docs.google.com/spreadsheets/d/1mOPHz0ZabGM4zJR8wvpwYPKiMeYRhPp08gP21WA47GA/edit?usp=sharing).

The screener notably detected Novavax, Inc. (NASD:NVAX) on April 17th at price $19.08. It is now priced $110.34, and reached a high of $189.40 in early August. This is an outlier compared to the rest of the data collected, however.

###### Requirements:

- Python 3
- Selenium (run "pip install selenium" in terminal to install)
- webdriver_manager ("pip install webdriver_manager" to install)



###### Notes:

  1. You must have a database of stock prices for this to work. I have included the av-bot.py file to do this. This is a selenium bot file that uses your AlphaVantage key to download the necessary csv files for your analysis. Adjust the time.sleep() parameter in the av-bot.py file to make this sufficiently slow if you have a free AlphaVantage account. See their website for information on their rates. The default time parameter is 20 seconds, which is slow. Adjust as needed.
  
  2. The stock-names.txt file by default contains the tickers of all companies listed on the NASDAQ. If you want to analyze some subset of these tickers, adjust this file.
  
 
