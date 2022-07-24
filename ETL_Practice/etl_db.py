import os
import sys
import mysqlx
import petl as etl
import configparser
import datetime
import json
import decimal
import requests


# retrieving data from our config file
config = configparser.ConfigParser()
try:
    config.read(r'ETL_Practice\etldemo.ini') # r turns string into raw string
    # terminal only recognizes a relative path while Jupyter Notebooks recognize the file
except Exception as e:
    print('Could not read configuration' + str(e))
    sys.exit()

# reading config parameters from config file
startDate = config['CONFIG']['startdate']
url = config['CONFIG']['url']
destServer = config['CONFIG']['server']
destDatabase = config['CONFIG']['database']

# request URL data
try:
    url_response = requests.get(url + startDate)
except Exception as e:
    print('Could not read url' + str(e))
    sys.exit()

# create list of lists
url_response_dates = []
url_response_rates = []

# check response status and add json data
if(url_response.status_code == 200):
    url_raw = json.loads(url_response.text)

    # extract data into columns
    for r in url_raw['observations']:
        url_response_dates.append(datetime.datetime.strptime(r['d'], '%Y-%m-%d'))
        url_response_rates.append(decimal.Decimal(r['FXUSDCAD']['v']))
    
    # create table with petl
    exchangeRates = etl.fromcolumns([url_response_dates, url_response_rates], header = ['date', 'rate'])

    # try loading expenses doc
    try:
        expenses = etl.io.fromxlsx(r'ETL_Practice\Expenses.xlsx')
    except Exception as e:
        print('Could not find the xlsx document' + str(e))
        sys.exit()

    # join tables with petl
    expenses = etl.outerjoin(exchangeRates, expenses, key = 'date')

    # we will fill missing values
    expenses = etl.filldown(expenses, 'rate')

    # removing data without expenses
    expenses = etl.select(expenses, lambda x: x.USD != None)

    # adding CAD column
    expenses = etl.addfield(expenses, 'CAD', lambda x: decimal.Decimal(x.USD) * x.rate)
    # it can be rounded: lambda x: round(decimal.Decimal(x.USD) * x.rate) to make it cleaner