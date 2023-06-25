import websockets
from producer import MyProducer
from consumer import MyConsumer
import json
import asyncio
from binance_streams_config import WSS_BINANCE,STREAM_BINANACE
from config import config
import websocket
import random
from utils import normalize_kline,normalize_kline_json,get_random_kline_data,handle_stream_msg




async def test_stream(API_KEY,topic,bootstrap_servers):
    producer = MyProducer(topic,bootstrap_servers)
    print(topic)
    idx = 0
    while True:
        msg = await get_random_kline_data(idx)
        idx += 1
        try:
            data = await normalize_kline_json(msg)
            print("messge: ",data,"\n")
        except Exception as e:
            print(e)
        await asyncio.sleep(3)

async def test_binance_stream(API_KEY,topic,bootstrap_servers):
    producer = MyProducer(topic,bootstrap_servers)
    print(topic)
    idx = 0
    while True:
        msg = await get_random_kline_data(idx)
        idx += 1
        try:
            data = await normalize_kline_json(msg)

            sanity_check = await producer.process_websocket_data(json.dumps(data))

        except Exception as e:
            print(e)
        await asyncio.sleep(3)


async def binance_stream(API_KEY,topic,bootstrap_servers):
    wss_delay = 30
    reconnect_delay= 5
    uri = WSS_BINANCE + STREAM_BINANACE
    headers = {
        'X-MBX-APIKEY': API_KEY
    }
    producer = MyProducer(topic,bootstrap_servers)
    num_reconnecting=5
    reconnect =0
    while True:
        try:
            async with websockets.connect(uri, extra_headers=headers) as websocket:                
                while True:

                    try:
                        response = await websocket.recv()
                        msg = json.loads(response)
                        data = await handle_stream_msg(msg)
                        # dd = msg.copy()
                        # d = dd['k'].copy()
                        # del dd['k']
                        # del dd['s']
                        # d['E'] = dd['E']
                        # d['e'] = dd['e']
                        sanity_check = await producer.process_websocket_data(json.dumps(data))

                    except websockets.exceptions.ConnectionClosed as e:
                        print("Connection closed.")
                        print(e)
                        break
                    await asyncio.sleep(wss_delay)

        except KeyboardInterrupt as e:
            print("stoppd")
            break
        except Exception as e:
            print(e)
            if reconnect == num_reconnecting:
                print("couldnt reconnect")
                break            
            print(f"reconnecting...{reconnect + 1}")
            reconnect += 1

            await asyncio.sleep(reconnect_delay)
            continue
# ws.on('ping', (e) => { //Defines callback for ping event
#     ws.pong(); //send pong frame
# });


async def kafka_stream(topic,bootstrap_servers):
    consumer = MyConsumer(topic,bootstrap_servers)
    await consumer.handle_kafka_messages()
  
    


