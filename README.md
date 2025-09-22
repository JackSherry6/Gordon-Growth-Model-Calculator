# Gordon Growth Model Calculator

A Python application that analyzes a stock’s future value based on dividends using the **Gordon Growth Model**.

## Overview

This program calculates the projected future value of any stock available in the **yfinance** library using the Gordon Growth Model. Key features include:

- **Data Sources**: Historical stock prices, historical dividends, systemic risk, and current market values based on the S&P 500.
- **Best Use Case**: The model assumes a **constant growth rate**, making it ideal for **well-established companies with stable growth**.
- **Interface**: A simple **Tkinter GUI** for easy input and results.
- **Backend**: Uses `yfinance`, `requests`, and `BeautifulSoup` to fetch and process stock and market data.

---

## Installation & Usage

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/Gordon-Growth-Model-Calculator.git
   cd Gordon-Growth-Model-Calculator

2. **Install required libraries**
    ```bash
    pip install yfinance requests beautifulsoup4

(Tkinter is included with most Python distributions. If missing, install via your OS package manager.)

3. **Run the program**
   ```bash
   python Gordon_Growth_Model_Calculator.py

## How it works
  1. Enter the stock symbol (e.g., `AAPL`).
  2. The program retrieves historical data and calculates the expected future value using the Gordon Growth formula: P=r−gD1​​

      Where:  
      - `P` = Stock value  
      - `D1` = Next year’s expected dividend  
      - `r` = Required rate of return (accounts for systemic risk)  
      - `g` = Expected constant growth rate

## Requirements

- Python 3.8+  
- Tkinter  
- yfinance  
- requests  
- BeautifulSoup4  

---

## Future Improvements

- Include **graphical visualizations** of dividend growth and stock projections.  
