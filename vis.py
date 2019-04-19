# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 23:15:46 2018

@author: kanha
"""

import matplotlib.pyplot as plt
import sys
import calculations as ca

def visualise(ticker):
    
    monthly = ca.monthly(ticker)
    print('Monthly return')
    print(monthly)
    print('-'*40)
    ax1 = monthly.plot()
    ax1.set_title('Monthly return')
    plt.show()
    
    yearly = ca.yearly(ticker)
    print('Yearly return')
    print(yearly)
    print('-'*40)
    ax2 = yearly.plot()
    ax2.set_title('Yearly return')
    plt.show()
    
    daily = ca.daily(ticker)
    ax3 = daily.plot()
    ax3.set_title('Daily return')
    plt.show()
    
    print('standard deviation ')
    print( daily.std())

ticker=[]
for grp in sys.argv[1:]:
  ticker.append(grp)
  
ticker.extend(['SPY','dummy_SPY'])
visualise(ticker)