#Title: Scanner.py
#Authors: Wanderer and Bohdi
#Date: 02/29/2021
#Purpose:	
# Provide a basic scanner that accepts a ticker input
# and returns the following information:
# 1.) - Key Statistics -
#	- previous close 
# 	- previous open
# 	- days range
# 	- 52 week range
# 	- volume
# 	- avg volume
# 	- mkt cap
# 	- 5y monthly beta
# 	- next earnings date
# 2.) - Financial Information -
#	- Income Statement
#	- Balance Sheet
#	- Cash Flow Statement
#	- Key Metric Ratios 
#import modules
import pandas as pd

class Scanner:
	
	# function that generates keystatistical information on a user inputed ticker
	def statistics	
		#Ticker input
		company = input('Enter Company Ticker Symbol')
		
		#--Statistics page--
		#URL to pull data from
		dataSourceStats = f'https://finance.yahoo.com/quote/{company}/key-statistics?p={company}'
		
		#read_html from selected dataSource URL using Pandas
		df1 = pd.read_html(dataSourceStats)
		
		#Data frames separated
		valuationMeasures = df1[0]
		stockPriceHistory = df1[1]
		shareStatistics = df1[2]
		dividendInfo = df1[3]
		profitabilityInfo = df1[5]
		managementEfectiveness = df1[6]
		incomeStatement = df1[7]
		balanceSheet = df1[8]
		cashFlow = df1[9]

		#Individual row output selections
		FiftyDMovAvg = stockPriceHistory.filter(like = '5', axis=0)

		print(FiftyDMovAvg)
		
		#Export results to excel
		valuationMeasures.to_excel('test.xlsx')

	def financials
	#User Ticker Input
		company1 = input('Enter Company Ticker Symbol')

		#--Financials Page--
		datasourceFinancials = f'https://finance.yahoo.com/quote/{company1}/financials?p={company1}'

		#scrapes the html from the user inputed datasource  financial search query
		df2 = pd.read_html(datasourceFinancials)

#End of Scanner class