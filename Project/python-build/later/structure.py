class DataSource:
    pass

class WebSocketAPI:
    pass

class DataSourceWebSocket(DataSource):
    def __init__(self,websocket_api: WebSocketAPI) -> None:
        super().__init__()
        self.websocket_api = websocket_api


class BinanceAPI(WebSocketAPI):
    def __init__(self) -> None:
        super().__init__()

class DataSourcesConfig():
    pass

# apis_config={
#     "binance":{
#         "streams":"",
#         'X-MBX-APIKEY': "API_KEY",
#         "websocket":"wss://stream.binance.com:9443/ws/",
#         "rest":""
#     }
# }