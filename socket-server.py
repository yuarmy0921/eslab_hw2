#!/usr/bin/env python3

import socket
import json
import numpy as np
import matplotlib.pyplot as plot
HOST = '192.168.175.63' # IP address
PORT = 6531 # Port to listen on (use ports > 1023)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Starting server at: ", (HOST, PORT))
    conn, addr = s.accept()
    with conn:
        print("Connected at", addr)
        conn.send(b'1')
        while True:
            data = conn.recv(1024).decode('utf-8', errors='ignore')
            #print(unicode(data, errors='replace'))
            print("Received from socket server:", data)
            
        if (data.count('{') != 1):
            # Incomplete data are received.
            # Some codes here
            pass
        print(data)
        '''
        obj = json.loads(data)
        t = obj['s']
        plot.scatter(t, obj['x'], c='blue') # x, y, z, gx, gy, gz
        # some codes here
        plot.xlabel("sample num")
        plot.pause(0.0001)
        '''