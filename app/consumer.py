import pika 

class RabbitmqConsumer:

    def __init__(self, callback) -> None:

        self.__host = "localhost"
        self.__port = 5672
        self.__user = "guest"
        self.__password = "guest"
        self.__queue = "data_queue"
        self.__callback = callback
        self.__channel = self.create_channel()



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

        channel.queue_declare(
            queue= self.__queue,
            durable=True
        )

        channel.basic_consume(

            queue= "data_queue",
            auto_ack= True,

            # aparentemente muito importante -->
            on_message_callback= self.__callback
        )

        return channel
    

    def start(self):
        print(f'Listen RabbitMQ on port ...')
        self.channel.start_consuming()

def minha_callback(ch, method, properties, body):
    print(body)

rmq = RabbitmqConsumer(minha_callback)
rmq.start()