# Funções RabbitMQ - Programador Lhama

RabbitMQ é um servidor de mensageria que permite que diferentes partes de um sistema se comuniquem de forma assíncrona por meio do envio e recebimento de mensagens. Ele gerencia filas de mensagens entre sistemas.

Ele funciona como um intermediário (message broker):

> Um produtor envia mensagens para uma fila dentro do RabbitMQ.
> Um consumidor lê e processa essas mensagens da fila.

Por padrão, as mensagens ficam na memória, o que é rápido, mas volátil (perde tudo se o servidor cair).

Se você quiser que elas persistam no disco, basta configurar:

- a fila como ` durable `
e 
- as mensagens como `persistent`.

Assim, mesmo que o RabbitMQ reinicie, as mensagens continuam salvas e serão entregues depois.