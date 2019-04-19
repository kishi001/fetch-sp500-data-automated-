# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 21:42:31 2018

@author: kanha
"""

import pandas as pd



#data.Date = pd.to_datetime(data.Date)
#data.set_index('Date',inplace=True)

def monthly(ticker):
    data = pd.read_csv(r'sp500_joined_closes.csv')
    data.Date = pd.to_datetime(data.Date)
    data.set_index('Date',inplace=True)
    
    monthly = data.copy()
    monthly = monthly.resample('BM').apply(lambda x:x[-1])
    monthly = monthly.pct_change()
    monthly['dummy_SPY']=monthly.iloc[:,:-1].mean(axis=1)
    monthly_return = monthly[ticker]
    
    return monthly_return
    

def yearly(ticker):
    data = pd.read_csv(r'sp500_joined_closes.csv')
    data.Date = pd.to_datetime(data.Date)
    data.set_index('Date',inplace=True)
    
    yearly = data.copy()
    yearly = yearly.resample('BA').apply(lambda x:x[-1])
    yearly = yearly.pct_change()
    yearly['dummy_SPY'] = yearly.iloc[:,:-1].mean(axis=1)
    yearly_return = yearly[ticker]
    return yearly_return
    

def daily(ticker):
    data = pd.read_csv(r'sp500_joined_closes.csv')
    data.Date = pd.to_datetime(data.Date)
    data.set_index('Date',inplace=True)
    
    daily_return = data.copy()    
    daily_return = daily_return.pct_change()
    daily_return['dummy_SPY']=daily_return.iloc[:,:-1].mean(axis=1) 
    daily_return = daily_return[ticker]
    return daily_return
    