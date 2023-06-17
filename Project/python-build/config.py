import os

class Config():
    pass


class DataFetcher(Config):
    API_KEY = os.environ.get('BINANCE_API_KEY')
    SECRET_KEY = os.environ.get('BINANCE_SECRET_KEY')


class TestConfig(Config):
    TEST_KEY = "key"
    TEST_TOPIC = "my_topic"

config = TestConfig()