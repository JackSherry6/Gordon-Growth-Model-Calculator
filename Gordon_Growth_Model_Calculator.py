import yfinance as yf
import numpy as np
from sklearn.linear_model import LinearRegression
import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk

def get_Model():
    stock_input = entry1.get()
    
    if yf.Ticker(stock_input).info == None:
        print("Invalid Abbreviation")

    stock = yf.Ticker(stock_input)
    spx = yf.Ticker("^GSPC")

    historical_stock_data = stock.history(period="5y")
    historical_spx_data = spx.history(period="5y")

    stock_values = []
    divs = []
    spx_values = []
    for i in range(len(historical_stock_data)):
        stock_values.append(historical_stock_data["Close"].iloc[i])
        divs.append(historical_stock_data["Dividends"].iloc[i])
        spx_values.append(historical_spx_data["Close"].iloc[i])

    R_stock = []
    R_spx = []
    for i in range(len(stock_values)-1):
        R_stock.append((((stock_values[i+1] + divs[i+1]) - stock_values[i])/stock_values[i])*100)
        R_spx.append(((spx_values[i+1] - spx_values[i])/spx_values[i])*100)

    Rstock_Rstock = []
    Rspx_Rspx = []
    Rstock_Rspx = []
    for i in range(len(R_stock)):
        Rstock_Rstock.append((R_stock[i] - np.mean(R_stock)) ** 2)
        Rspx_Rspx.append((R_spx[i] - np.mean(R_spx)) ** 2)
        Rstock_Rspx.append((R_stock[i] - np.mean(R_stock)) * (R_spx[i] - np.mean(R_spx)))
        
    variance_spx = (np.sum(Rspx_Rspx) / (len(Rspx_Rspx)-1))
    covariance = (np.sum(Rstock_Rspx) / (len(Rstock_Rspx)-1))

    systemic_risk = covariance / variance_spx

    r = requests.get("https://www.stock-analysis-on.net/NASDAQ/Company/Microsoft-Corp/DCF/CAPM?srsltid=AfmBOorZwUVKFpSSidlhZyKPhmt7JxcNnuNv1MnysfXwT1Z_UcvgrYHA#Rates-of-Return")
    soup = BeautifulSoup(r.content, 'html5lib')
    table = soup.find('span', attrs = {'class':'paywall'}) 

    Rf = 0
    E_Rm = 0
    cnt = 0
    for row in table.find_all_next('span', attrs = {'class': 'paywall'}):
        cnt = cnt + 1
        if cnt == 33:
            E_Rm = row.text
        if cnt == 34:
            Rf = row.text
    Rf = float(Rf[:-1])
    E_Rm = float(E_Rm[:-1])
            
    previous_yr_div = ((historical_stock_data["Close"].iloc[-252] / 10) * (stock.dividends.iloc[-4] / 10))
    currentPrice = historical_stock_data["Close"].iloc[-1]

    RRoR = Rf + systemic_risk * (E_Rm - Rf)

    GGModel = (currentPrice * RRoR - previous_yr_div) / (currentPrice + previous_yr_div)
    GGModel = str(GGModel)
    GGModel = stock_input + " dividend value: " + GGModel[0:6]
    
    label = tk.Label(root, height=5, font=('Segoe 12'), text=GGModel)
    #label.destroy()
    label.pack()
    print(GGModel)
    

root = tk.Tk()
root.title("Stock Growth Analysis")
root.geometry("500x500")

label1 = tk.Label(root, text="Enter stock abbreviation below")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

calcButton = tk.Button(root, text="Enter", command=get_Model)
calcButton.pack()

root.mainloop()