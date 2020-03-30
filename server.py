import socket
import select


HEADER_LENGTH=10
IP="127.0.0.1"
port 1234


server_socket=socket.socket(socket.AF_INET,socket.SOFT_SOFTSTREAM)
server_socket.setsockopt(socket.SOL_SOCKET.socket.SO_REUSEADDR,1)

server_socket.bind((IP,PORT))
server_socket.listen()

sockets_list=[server_socket]
