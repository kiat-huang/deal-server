#!/usr/bin/env python

# messaging.py
# Messaging bus for game play
# Kiat Huang <kiat.huang@gmail.com>

import sys
import json
import pika

# get player's table key, seat key and bid    
# example argument format '{"mytablekey": "MpnH72Sm", "myseatkey": "9fVNgmipwOPpeJ7olJ3nrqALbhRvOjL4", "mybid": "1N"}'
args = json.loads(sys.argv[1])

table_key = args.get("mytablekey")
seat_key = args.get("myseatkey")
bid = args.get("mybid") 

# create a messaging bus
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost'))
channel = connection.channel()
# declare the queue with the supplied table key
channel.queue_declare(queue = table_key, durable=True)

# publish a bid!
channel.basic_publish(exchange = '', 
    routing_key = table_key,
    body = sys.argv[1],
    properties=pika.BasicProperties(
        delivery_mode = 2 # make message persistent
        ))

print(" [x] Sent " + table_key)

connection.close()

