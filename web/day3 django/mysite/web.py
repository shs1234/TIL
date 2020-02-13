# https://soooprmx.com/archives/8737
import socket
from datetime import datetime
import subprocess

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP/IP

server_socket.bind(('localhost', 80)) #아이피 주소, 포트
server_socket.listen(0)
print('listening')

client_socket, addr = server_socket.accept()
print('accepting')

data = client_socket.recv(65535) # 64비트(8바이트)로 받음.
print('receive : '+data.decode())

# client_socket.send(data)
# print('send data')
client_socket.close()
print('종료')