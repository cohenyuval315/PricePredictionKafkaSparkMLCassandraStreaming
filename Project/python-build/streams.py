import websockets
from producer import MyProducer
from consumer import MyConsumer
import json
import asyncio
from binance_config import WSS_BINANCE,STREAM_BINANACE
from config import config


async def normalize_kline(msg):
    data = msg['k']
    coin = data['s']
    high = data['h']
    low = data['l']
    timestamp = data['t']
    data_string = f'timestamp:{timestamp}|coin:{coin}|high:{high}|low:{low}'
    return data_string


async def binance_stream(API_KEY,topic,bootstrap_servers):
    wss_delay = 30
    uri = WSS_BINANCE + STREAM_BINANACE
    headers = {
        'X-MBX-APIKEY': API_KEY
    }
    producer = MyProducer(topic,bootstrap_servers)

    
    async with websockets.connect(uri, extra_headers=headers) as websocket:
        while True:
            try:
                response = await websocket.recv()
                msg = json.loads(response)
                #msg= await normalize_kline(msg)
                msg = str(msg)
                sanity_check = await producer.process_websocket_data(msg)

            
            except websockets.exceptions.ConnectionClosed as e:
                print("Connection closed.")
                print(e)
                break

            await asyncio.sleep(wss_delay)



async def kafka_stream(topic,bootstrap_servers):
    consumer = MyConsumer(topic,bootstrap_servers)
    await consumer.handle_kafka_messages()
  
    


