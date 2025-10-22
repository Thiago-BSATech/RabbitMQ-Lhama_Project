import pika

def minha_callback(ch, method, properties, body):
    print(body)

connection_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

channel = pika.BlockingConnection(connection_parameters).channel()

channel.queue_declare(
    queue= "data_queue",
    durable=True
)

channel.basic_consume(

    queue= "data_queue",
    auto_ack= True,

    # aparentemente muito importante -->
    on_message_callback= minha_callback
)

print(f'Listen RabbitMQ on port ...')
channel.start_consuming()