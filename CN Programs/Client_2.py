# 2.Write a client/server program in python to
# demonstrate two way communication of client and server.

#Client.py

import socket
HOST = 'localhost'
PORT = 8030

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print('Connected to {}:{}'.format(HOST, PORT))

while True:
    message = input('Enter a message: ')
    client_socket.sendall(message.encode())
    data = client_socket.recv(1024).decode()
    print('Received response: {}'.format(data))

print('Closing connection')
client_socket.close()
