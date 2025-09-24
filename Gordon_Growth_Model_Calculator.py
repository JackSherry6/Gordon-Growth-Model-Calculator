import yfinance as yf
import numpy as np

def gordon_growth_model(stock, required_return=0.10, high_growth_years=5, stable_growth=0.03):  
    # To account for high-growth or low-dividend stocks, function will fall back onto a two-stage approach if it detects them
    """
    Parameters:
    - required_return: expected annual return (r), I chose to use 10% because it is commonly used as standard in the industry
    - high_growth_years: years of high initial growth (for two-stage GGM)
    - stable_growth: long-term stable growth rate (g)
    """
    # Get dividend data
    stock = yf.Ticker(stock)
    dividends = stock.dividends

    if dividends.empty:
        return f"{stock}: No dividends, GGM not applicable"

    # Last dividend
    D0 = dividends.iloc[-1]

    # Calculate historical growth rate based on last 5 dividends
    historical_divs = dividends.iloc[-5:]
    if len(historical_divs) < 2:
        g = stable_growth  # fallback to stable growth if there are less than 2 historical dividends to go off of
    else:
        g = np.mean([historical_divs.iloc[i] / historical_divs.iloc[i-1] - 1 for i in range(1, len(historical_divs))])

    #Get current stock price
    curr_val = stock.info.get('currentPrice') or stock.history(period='1d')['Close'].iloc[-1]
    
    # Single-stage GGM if growth < required return
    if g < required_return:
        P = D0 * (1 + g) / (required_return - g)
        return f"{stock}: Current value: {curr_val:.2f}, Value by standard GGM = ${P:.2f}, g = {g:.2%}, r = {required_return:.2%}"

    # Two-stage GGM for high-growth stocks
    else:
        # Project dividends for high-growth period
        D_high = [D0 * (1 + g)**(i+1) for i in range(high_growth_years)]
        # Terminal value using stable growth
        D_terminal = D_high[-1] * (1 + stable_growth) / (required_return - stable_growth)
        # Discount all dividends to present value
        PV = sum([D / (1 + required_return)**(i+1) for i, D in enumerate(D_high)]) \
             + D_terminal / (1 + required_return)**high_growth_years
        return f"{stock}: Current value: {curr_val:.2f}, Value by two-stage GGM = ${PV:.2f}, initial g = {g:.2%}, stable g = {stable_growth:.2%}"

if __name__ == "__main__":
    stock = input("Enter stock ticker (e.g. AAPL): ").strip().upper()
    result = gordon_growth_model(stock)
    print(result)
    
    
# to activate venv use command: venv\Scripts\activate.bat
