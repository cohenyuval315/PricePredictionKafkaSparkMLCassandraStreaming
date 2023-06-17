import asyncio
import os
from streams import binance_stream,kafka_stream
import sys
from config import config


from utils import readProperty


sys.path.append("..")
sys.path.append("/../.env")
sys.path.append("./../config.properties")
sys.path.append("/Desktop/Big Data/Project/")




CONFIG_PATH = '. /../config.properties'
TEMP_CONFIG_PATH = './temp.properties'
SECTION_NAME = 'SECTION_NAME'
TEST_TOPIC = "test_topic"
BOOTSRAP_SERVERS = "localhost:9092"

async def main():

    d = readProperty(TEMP_CONFIG_PATH,SECTION_NAME,"key1")
    print(d)


    API_KEY = os.environ.get('BINANCE_API_KEY')
    SECRET_KEY = os.environ.get('BINANCE_SECRET_KEY')
    kafka_topic = config.TEST_TOPIC
    kafka_test_key = config.TEST_KEY
    bootstrap_servers = BOOTSRAP_SERVERS

    await asyncio.gather(*[binance_stream(API_KEY,kafka_topic,bootstrap_servers),
                         kafka_stream(kafka_topic,bootstrap_servers)]
                                ,return_exceptions=True)
    


if __name__ == "__main__":
    asyncio.run(main())
