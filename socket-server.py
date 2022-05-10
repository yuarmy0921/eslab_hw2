#!/usr/bin/env python3

import socket
import json
import numpy as np
import matplotlib.pyplot as plot
HOST = '192.168.50.166' # IP address
PORT = 8080 # Port to listen on (use ports > 1023)
t_axis = []
x_plot = []
y_plot = []
z_plot = []
gx_plot = []
gy_plot = []
gz_plot = []
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Starting server at: ", (HOST, PORT))
    conn, addr = s.accept()
    with conn:
        print("Connected at", addr)
        #conn.send(b'1')
        while True:
            data = conn.recv(1024).decode('utf-8', errors='ignore')
            #print(unicode(data, errors='replace'))
            print("Received from socket server:", data)
            
        