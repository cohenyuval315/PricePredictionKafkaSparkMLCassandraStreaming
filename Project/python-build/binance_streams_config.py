

import enum

class TickerIntervals(enum.Enum):
    TICKER_1h = "1h"
    TICKER_4h = "4h"
    TICKER_1d = "1d"


class KlineIntervals(enum.Enum):
    KLINE_1s = "1s"
    KLINE_1m = "1m"
    KLINE_3m = "3m"
    KLINE_5m = "5m"
    KLINE_15m = "15m"
    KLINE_30m = "30m"
    KLINE_1h = "1h"
    KLINE_2h = "2h"
    KLINE_4h = "4h"
    KLINE_6h = "6h"
    KLINE_8h = "8h"
    KLINE_12h = "12h"
    KLINE_1d = "1d"
    KLINE_3d = "3d"
    KLINE_1w = "1w"
    KLINE_1M = "1M"




class BinanceStreamConfig():
    WSS_BINANCE = "wss://stream.binance.com:9443/"
    RAW_STREAM_SUFFIX = "ws/"
    COMBINED_STREAM_SUFFIX = "/streams?=" 

    DEPTH = "@depth"
    DEPTH_100 = "@depth@100"

    TICKER = "@ticker_"
    KLINE = "@kline_"

    TICKER_UPDATE_MS = 1000
    KLINE_UPDATE_MS_1s_interval = 1000
    KLINE_UPDATE_MS = 2000
    DEPTH_UPDATE_MS_100 = 100
    DEPTH_UPDATE_MS = 1000
    


    def __init__(self,symbol="btcusdt") -> None:
        self.symbol = symbol
        self.streams_data = []
        self.streams_url = ""

    def add_ticker_stream(self,interval:TickerIntervals):
        update_speed = self.TICKER_UPDATE_MS
        stream_name = f"{self.symbol}{self.TICKER}{interval}"
        self.streams_data.append({
            "stream":stream_name,
            "update":update_speed
        })

    def add_kline_stream(self,interval:KlineIntervals):
        if interval == "1s":
            update_speed = self.KLINE_UPDATE_MS_1s_interval
        else:
            update_speed = self.KLINE_UPDATE_MS
        stream_name = f"{self.symbol}{self.KLINE}{interval}"
        self.streams_data.append({
            "stream":stream_name,
            "update":update_speed
        })

    def add_book_stream(self,book_limit=1000,fast=False):
        if fast == False:
            update_speed = self.DEPTH_UPDATE_MS
            depth = self.DEPTH
        else:
            update_speed = self.DEPTH_UPDATE_MS_100
            depth = self.DEPTH_100
        book_snapshot = f"https://api.binance.com/api/v3/depth?symbol={self.symbol}&limit={book_limit}"
        stream_name = f"{self.symbol}{depth}"
        self.streams_data.append({
            "stream":stream_name,
            "update":update_speed,
            "book":book_snapshot,
        })

    def create_streams_url(self):
        if len(self.streams_data) == 0:
            return ""
        if len(self.streams_data) == 1:
            return self.WSS_BINANCE + self.RAW_STREAM_SUFFIX + self.streams_data[0]['stream']
        streams_names = [s["stream"] for s in self.streams_data]
        stream_url = "/".join(streams_names)
        if stream_url[0] == "/":
            stream_url = stream_url[1:]
        if stream_url[len(stream_url) - 1] == "/":
            stream_url = stream_url[:len(stream_url)-1]
        url = self.WSS_BINANCE + self.COMBINED_STREAM_SUFFIX + stream_url
        return url
    

    def get_num_of_streams(self):
        return len(self.streams_data)
    


WSS_BINANCE = "wss://stream.binance.com:9443/ws/"
BOOK_STREAM = "wss://stream.binance.com:9443/ws/btcusdt@depth"




# ticker :  
# <symbol>@ticker_<window_size>  TICKER STATISTICS
# 1h, 4h , 1d
# update 1 sec
# payload:
# {
#   "e": "1hTicker",    // Event type
#   "E": 123456789,     // Event time
#   "s": "BNBBTC",      // Symbol
#   "p": "0.0015",      // Price change
#   "P": "250.00",      // Price change percent
#   "o": "0.0010",      // Open price
#   "h": "0.0025",      // High price
#   "l": "0.0010",      // Low price
#   "c": "0.0025",      // Last price
#   "w": "0.0018",      // Weighted average price
#   "v": "10000",       // Total traded base asset volume
#   "q": "18",          // Total traded quote asset volume
#   "O": 0,             // Statistics open time
#   "C": 86400000,      // Statistics close time
#   "F": 0,             // First trade ID
#   "L": 18150,         // Last trade Id
#   "n": 18151          // Total number of trades
# }


# kline :
# <symbol>@kline_<interval>
# update 1 sec for 1s rest is 2 sec:
# 1s
# 1m
# 3m
# 5m
# 15m
# 30m
# 1h
# 2h
# 4h
# 6h
# 8h
# 12h
# 1d
# 3d
# 1w
# 1M
#payload:
# {
#   "e": "kline",     // Event type
#   "E": 123456789,   // Event time
#   "s": "BNBBTC",    // Symbol
#   "k": {
#     "t": 123400000, // Kline start time
#     "T": 123460000, // Kline close time
#     "s": "BNBBTC",  // Symbol
#     "i": "1m",      // Interval
#     "f": 100,       // First trade ID
#     "L": 200,       // Last trade ID
#     "o": "0.0010",  // Open price
#     "c": "0.0020",  // Close price
#     "h": "0.0025",  // High price
#     "l": "0.0015",  // Low price
#     "v": "1000",    // Base asset volume
#     "n": 100,       // Number of trades
#     "x": false,     // Is this kline closed?
#     "q": "1.0000",  // Quote asset volume
#     "V": "500",     // Taker buy base asset volume
#     "Q": "0.500",   // Taker buy quote asset volume
#     "B": "123456"   // Ignore
#   }
# }

# book :
# Stream Name: <symbol>@depth OR <symbol>@depth@100ms
# Update Speed: 1000ms or 100ms
# payload: 
# {
#   "e": "depthUpdate", // Event type
#   "E": 123456789,     // Event time
#   "s": "BNBBTC",      // Symbol
#   "U": 157,           // First update ID in event
#   "u": 160,           // Final update ID in event
#   "b": [              // Bids to be updated
#     [
#       "0.0024",       // Price level to be updated
#       "10"            // Quantity
#     ]
#   ],
#   "a": [              // Asks to be updated
#     [
#       "0.0026",       // Price level to be updated
#       "100"           // Quantity
#     ]
#   ]
# }

# # for book first get snapshot :
# How to manage a local order book correctly
# Open a stream to wss://stream.binance.com:9443/ws/bnbbtc@depth.
# Buffer the events you receive from the stream.
# Get a depth snapshot from https://api.binance.com/api/v3/depth?symbol=BNBBTC&limit=1000 .
# Drop any event where u is <= lastUpdateId in the snapshot.
# The first processed event should have U <= lastUpdateId+1 AND u >= lastUpdateId+1.
# While listening to the stream, each new event's U should be equal to the previous event's u+1.
# The data in each event is the absolute quantity for a price level.
# If the quantity is 0, remove the price level.
# Receiving an event that removes a price level that is not in your local order book can happen and is normal.
# Note: Due to depth snapshots having a limit on the number of price levels, a price level outside of the initial snapshot that doesn't have a quantity change won't have an update in the Diff. Depth Stream. Consequently, those price levels will not be visible in the local order book even when applying all updates from the Diff. Depth Stream correctly and cause the local order book to have some slight differences with the real order book. However, for most use cases the depth limit of 5000 is enough to understand the market and trade effectively.


STREAM_BINANACE = "btcusdt@kline_1m"

STREAM_BINANACE_TRADE = "btcusdt@trade"
REST_API = "wss://ws-api.binance.com:443/ws-api/v3"
URL = "https://github.com/binance/binance-public-data/#klines"
STREAMS_BINANCE = {
    "btcusdt@kline_1m":{
        "delay":1
    }

}
# The base endpoint is: wss://stream.binance.com:9443 or wss://stream.binance.com:443
# Streams can be accessed either in a single raw stream or in a combined stream.
# Users can listen to multiple streams.
# Raw streams are accessed at /ws/<streamName>
# Combined streams are accessed at /stream?streams=<streamName1>/<streamName2>/<streamName3>
# Combined stream events are wrapped as follows: {"stream":"<streamName>","data":<rawPayload>}
# All symbols for streams are lowercase
# A single connection to stream.binance.com is only valid for 24 hours; expect to be disconnected at the 24 hour mark
# The websocket server will send a ping frame every 3 minutes. If the websocket server does not receive a pong frame back from the connection within a 10 minute period, the connection will be disconnected. Unsolicited pong frames are allowed.
# The base endpoint wss://data-stream.binance.vision can be subscribed to receive market data messages. User data stream is NOT available from this URL.