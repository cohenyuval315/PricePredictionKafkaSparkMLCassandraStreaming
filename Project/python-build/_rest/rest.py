import requests
import os
def get_historical_candles(symbol, interval, start_time, end_time):
    url = "https://api.binance.com/api/v3/klines"
    
    params = {
        "symbol": symbol,
        "interval": interval,
        "startTime": start_time,
        "endTime": end_time,
        "limit": 1000  # Maximum limit per request (adjust as needed)
    }
    API_KEY = os.environ.get('BINANCE_API_KEY')
    headers = {
        'X-MBX-APIKEY': API_KEY
    }
    
    response = requests.get(url, params=params,headers=headers)
    
    if response.status_code == 200:
        candles = response.json()
        return candles
    else:
        print("Error:", response.status_code)
        return None

symbol = "BTCUSDT"  # Symbol of the trading pair
interval = "1d"  # Interval for 1-day candles
start_time = 1622534400000  # Start timestamp (in milliseconds) - Adjust to the desired start time
end_time = 1625135999000  # End timestamp (in milliseconds) - Adjust to the desired end time

candles = get_historical_candles(symbol, interval, start_time, end_time)

if candles:
    for candle in candles:
        print(candle)
