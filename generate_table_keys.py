#!/usr/bin/env python

# generate_table_keys.py
# generates a bunch of table_keys and writes them as a JSON object to a file
# Kiat Huang <kiat.huang@gmail.com>

import sys
import json
import random
import string

if __name__ == "__main__":

    table_keys = {}
    table_key_length = 16

    # create file with the play_id
    filestring = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(table_key_length)])
    filepath = ''.join(["outputs/tablekeys.",filestring,".json"])

    table_tuple = {}
    
    for i in range(0,100):
        table_keys[i] = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(table_key_length)])
        table_tuple.update({i: table_keys[i]}) 

    # create the immutable table_json object
    table_json = json.dumps(table_tuple, indent = 4)
    print(table_json)

    with open(filepath,"w+") as outfile:
        json.dump(table_tuple, outfile)
    
   