from configparser import ConfigParser
import random

@staticmethod
def readProperty(path,section,key):
    config = ConfigParser()
    config.read(path)
    test = config.get(section,key)
    return test

@staticmethod
def readSection(path,section):
    config = ConfigParser()
    config.read(path)
    test = config.get(section)
    return test

@staticmethod
def readPropertiesFile(path):
    config = ConfigParser()
    config.read(path)
    test = config.get()
    return test

async def get_snapshot():
    symbol = "BTCUSDT"
    limit = 1000
    url = f"https://api.binance.com/api/v3/depth?symbol={symbol}&limit={limit}"
    ##

    ##
    json = {}
    data = {
        "lastUpdateId":int(json["lastUpdateId"]),
        "bids":json['bids'],
        "asks":json['asks'],
    }
    return data

async def handle_stream_msg(msg):
    kline = "kline"
    ticker = "Ticker"
    depth = "depthUpdate"
    event_type = msg['e']
    if kline in event_type:
        normal_msg = await normalize_kline(msg)
        data = await normalize_kline_json(normal_msg)
        return data
    if ticker in event_type:
        normal_msg = await normalize_ticker(msg)
        data = await normalize_ticker_json(normal_msg)
        return data  
    if depth in event_type:
        normal_msg = await normalize_depth(msg)
        data = await normalize_depth_json(normal_msg)
        return data

async def normalize_depth(msg):
    return msg

async def normalize_depth_json(json):
    data = {
        "depthUpdate":str(json["e"]), # : "depthUpdate", // Event type
        "eventTime":int(json["E"]), # : 123456789,     // Event time
        "symbol":str(json["s"]), # : "BNBBTC",      // Symbol
        "firstUpdateID":int(json["U"]), # : 157,           // First update ID in event
        "finalUpdateID":int(json["u"]), # : 160,           // Final update ID in event

        "bids":json["b"], # : [              // Bids to be updated
        #     [
        #       "0.0024",       // Price level to be updated
        #       "10"            // Quantity
        #     ]
        #   ],
        "asks":json["a"], # : [              // Asks to be updated
        #     [
        #       "0.0026",       // Price level to be updated
        #       "100"           // Quantity
        #     ]
        #   ]
    }

    return data

async def normalize_ticker(msg):
    return msg

async def normalize_ticker_json(json):
    data = {
    "eventType" : str(json["e"]), #: "1hTicker",    // Event type
    "eventTime" :int(json["E"]), #: 123456789,     // Event time
    "symbol" : str(json["s"]), #: "BNBBTC",      // Symbol
    "priceChange" :float(json["p"]), #: "0.0015",      // Price change
    "priceChangePercent" :float(json["P"]), #: "250.00",      // Price change percent
    "openPrice" :float(json["o"]), #: "0.0010",      // Open price
    "highPrice" :float(json["h"]), #: "0.0025",      // High price
    "LowPrice" :float(json["l"]), #: "0.0010",      // Low price
    "lastPrice" :float(json["c"]), #: "0.0025",      // Last price
    "weightedAveragePrice" :float(json["w"]), #: "0.0018",      // Weighted average price
    "totalTradedBaseAssetVolume" :float(json["v"]), #: "10000",       // Total traded base asset volume
    "totalTradedQuoteAssetVolume" :float(json["q"]), #: "18",          // Total traded quote asset volume
    "statisticsOpenTime" :float(json["O"]), #: 0,             // Statistics open time
    "statisticsCloseTime" :float(json["C"]), #: 86400000,      // Statistics close time
    "firstTradeID" :int(json["F"]), #: 0,             // First trade ID
    "lastTradeID" :int(json["L"]), #: 18150,         // Last trade Id
    "totalNumberOfTrades" :int(json["n"]), #: 18151          // Total number of trades
    }
    return data

async def normalize_kline(msg):
    m = msg.copy()
    normal_msg = m['k'].copy()
    del m['k']
    del m['s']
    normal_msg['E'] = m['E']
    normal_msg['e'] = m['e'] 
    return normal_msg

async def normalize_kline_json(json):
    data = {
      "eventType": str(json['e']),
      "eventTime": int(json["E"]),
      "symbol": str(json["s"]),
      "klineStartTime": int(json["t"]),
      "klineCloseTime": int(json["T"]),
      "interval": str(json["i"]), 
      "firstTradeID": int(json["f"]), 
      "lastTradeID": int(json["L"]), 
      "openPrice": float(json["o"]), 
      "closePrice": float(json["c"]), 
      "highPrice": float(json["h"]), 
      "lowPrice": float(json["l"]), 
      "baseAssetVolume": float(json["v"]), 
      "numOfTrades": int(json["n"]), 
      "klineClosed": bool(json["x"]),
      "quoteAssetVolume": float(json["q"]), 
      "takerBuyBaseAssetVolume": float(json["V"]), 
      "takerBuyQuoteAssetVolume": float(json["Q"]), 
      "ignore": str(json["B"]),
    }
    return data

async def get_random_ticker_data(idx):
    symbol = "BTCUSD"
    eventType = "kline"
    E = 123456789 + idx
    interval = "1m"
    end_start = 60000
    o = random.randint(10,30) / 10000.0
    c = random.randint(10,30) / 10000.0
    h = random.randint(10,30) / 10000.0
    l = random.randint(10,30) / 10000.0
    B = random.randint(100000,999999)
    n = random.randint(10,100)
    data = {
      "e": eventType,#     // Event type
      "E": E,#   // Event time
      "s": symbol,#    // Symbol
      "t": 123400000,# // Kline start time
      "T": 123460000,# // Kline close time
      "i": interval,#      // Interval
      "f": 100 + idx,#       // First trade ID
      "L": 200 + idx,#       // Last trade ID
      "o": f"{o}",#  // Open price
      "c": f"{c}",#  // Close price
      "h": f"{h}",#  // High price
      "l": f"{l}",#  // Low price
      "v": "1000",#    // Base asset volume
      "n": n,#       // Number of trades
      "x": False,#     // Is this kline closed?
      "q": "1.0000",#  // Quote asset volume
      "V": "500",#     // Taker buy base asset volume
      "Q": "0.500",#   // Taker buy quote asset volume
      "B": f"{B}" # Ignore
    }
    return data

async def get_random_depth_data(idx):
    symbol = "BTCUSD"
    eventType = "kline"
    E = 123456789 + idx
    interval = "1m"
    end_start = 60000
    o = random.randint(10,30) / 10000.0
    c = random.randint(10,30) / 10000.0
    h = random.randint(10,30) / 10000.0
    l = random.randint(10,30) / 10000.0
    B = random.randint(100000,999999)
    n = random.randint(10,100)
    data = {
      "e": eventType,#     // Event type
      "E": E,#   // Event time
      "s": symbol,#    // Symbol
      "t": 123400000,# // Kline start time
      "T": 123460000,# // Kline close time
      "i": interval,#      // Interval
      "f": 100 + idx,#       // First trade ID
      "L": 200 + idx,#       // Last trade ID
      "o": f"{o}",#  // Open price
      "c": f"{c}",#  // Close price
      "h": f"{h}",#  // High price
      "l": f"{l}",#  // Low price
      "v": "1000",#    // Base asset volume
      "n": n,#       // Number of trades
      "x": False,#     // Is this kline closed?
      "q": "1.0000",#  // Quote asset volume
      "V": "500",#     // Taker buy base asset volume
      "Q": "0.500",#   // Taker buy quote asset volume
      "B": f"{B}" # Ignore
    }
    return data

async def get_random_kline_data(idx):
    symbol = "BTCUSD"
    eventType = "kline"
    E = 123456789 + idx
    interval = "1m"
    end_start = 60000
    o = random.randint(10,30) / 10000.0
    c = random.randint(10,30) / 10000.0
    h = random.randint(10,30) / 10000.0
    l = random.randint(10,30) / 10000.0
    B = random.randint(100000,999999)
    n = random.randint(10,100)
    data = {
      "e": eventType,#     // Event type
      "E": E,#   // Event time
      "s": symbol,#    // Symbol
      "t": 123400000,# // Kline start time
      "T": 123460000,# // Kline close time
      "i": interval,#      // Interval
      "f": 100 + idx,#       // First trade ID
      "L": 200 + idx,#       // Last trade ID
      "o": f"{o}",#  // Open price
      "c": f"{c}",#  // Close price
      "h": f"{h}",#  // High price
      "l": f"{l}",#  // Low price
      "v": "1000",#    // Base asset volume
      "n": n,#       // Number of trades
      "x": False,#     // Is this kline closed?
      "q": "1.0000",#  // Quote asset volume
      "V": "500",#     // Taker buy base asset volume
      "Q": "0.500",#   // Taker buy quote asset volume
      "B": f"{B}" # Ignore
    }
    return data


def interval_to_secs(interval:str):
    if interval == "1h":
        return 
    pass







