import pika
import json

from typing import Dict

class RabbitmqPublisher:

    def __init__(self, callback) -> None:

        self.__host = "localhost"
        self.__port = 5672
        self.__user = "guest"
        self.__password = "guest"
        self.__queue = "data_queue"
        self.__callback = callback
        self.__channel = self.__create_channel()
        self.__exchange = "data_exchange"
        self.routing_key = ""

    
    
    def __create_channel(self):

        connection_parameters = pika.ConnectionParameters(
            host = self.__host ,
            port = self.__port,
            credentials = pika.PlainCredentials( 

                username = self.__user,
                password = self.__password 
            )
        )


        channel = pika.BlockingConnection(connection_parameters).channel()
        return channel
    
    def send_message(self, body: Dict):

        self.__channel.basic_publish(

            exchange = self.__exchange,
            routing_key = self.routing_key,
            body = json.dumps(body),
            properties= pika.BasicProperties(
                delivery_mode = 2
            )
        )

rabbitP = RabbitmqPublisher()
rabbitP.send_message({ "message": "something"})