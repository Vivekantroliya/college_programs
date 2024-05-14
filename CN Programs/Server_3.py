# 3.Write a client/server program to demonstrate
# the communication on two different computer.

#Server.py

import socket
HOST = "172.21.17.139"
PORT = 12345

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))

s.listen(1)
print(f"Listening on {HOST} : {PORT}")

conn, addr = s.accept()
print(f"Connection established with {addr}")

message = "Welcome to the server!"
conn.send(message.encode())

data = conn.recv(1024).decode()
print(f"Received From Client : {data}")
conn.close()
