# Gordon Growth Model (GGM) Valuation Tool

This repository provides a Python implementation of the **Gordon Growth Model (GGM)**, with a built-in two-stage extension for high-growth stocks. The script fetches stock and dividend data using the `yfinance` library and estimates the intrinsic value of a stock based on expected dividend growth. Though the Gordon Growth Model is a rough predictor of stock performance, it can still provide useful insight when evaluating potential long-term holdings.

---

### Features
- **Single-stage GGM:** Values dividend-paying stocks under stable growth assumptions.  
- **Two-stage GGM:** Automatically switches to a two-stage model for high-growth or low-dividend stocks.  
- **Data-driven growth estimates:** Uses the historical dividend growth rate (when available).  
- **Fallback mechanisms:** If insufficient dividend data exists, falls back to a user-specified stable growth rate.  
- **Real-time stock data:** Pulls dividend history, growth rates, and current prices via Yahoo Finance.  

---

### Requirements
- Python 3.8+  
- pip dependencies:  
  - `yfinance`  
  - `numpy`  

Install all dependencies using:
   `pip install yfinance numpy`

---

### Usage
1. Clone this repository:

`bash
git clone https://github.com/yourusername/ggm-valuation.git

cd ggm-valuation`

2. Run the script:
   
`bash
python ggm.py`

3. Enter a stock ticker when prompted (e.g., `AAPL`, `MSFT`, `KO`).

**Example output:** `APPL: Current value: 58.34, Value by standard GGM = $62.11, g = 3.25%, r = 10.00%`
