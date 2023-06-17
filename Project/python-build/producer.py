from confluent_kafka import Producer
import json

class MyProducer():
    def __init__(self,topic,bootstrap_servers="localhost:9092",broker_id = 0) -> None:
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self.producer = Producer({'bootstrap.servers': self.bootstrap_servers })
        #self.producer = self.init_producer()

    def init_producer(self):
        producer_config = {
            'bootstrap.servers': self.bootstrap_servers,
            'key.serializer': str.encode,
            'socket.keepalive.enable': True,
            'value.serializer': lambda v: json.dumps(v).encode('utf-8')
        }
        producer = Producer(producer_config)
        return producer

    def acked(self,err, msg):
        if err is not None:
            print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
        else:
            print("Message produced: %s" % (str(msg)))

    async def process_websocket_data(self,data,key="key"):
        self.producer.produce(self.topic,key=key, value=data,callback=self.acked)
        return True
        #self.producer.flush() 
