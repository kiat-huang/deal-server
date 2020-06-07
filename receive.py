#!/usr/bin/env python

# messaging.py
# Messaging bus for game play
# Kiat Huang <kiat.huang@gmail.com>

import sys
import json
import pika

# get user's submitted table_key    
# example argument format '{"mytablekey" : "MpnH72Sm"}'
args = json.loads(sys.argv[1])
user_table_key = args.get("mytablekey")

# create a messaging bus
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue = user_table_key,durable=True)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag = method.delivery_tag)
 
channel.basic_consume(queue = user_table_key,
   # auto_ack = True,
   on_message_callback = callback)
   
print(" [*] Waiting for messages from game " + user_table_key + "To exit press CTRL+C")

channel.start_consuming()