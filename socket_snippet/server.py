# import socket
# HOST = 'localhost' 
# PORT = 3000 
# s = socket.socket()
# s.bind((HOST, PORT)) 
# s.listen() 
# print("Server runing in port ", PORT) 
# while True:
#     conn, addr = s.accept() 
#     res = conn.recv(1024)
#     print('New conection', addr)
#     print(res) 
#     conn.send(b' Hello from server!')
#     conn.close()

import socket

HOST = "localhost"
PORT = 3000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"Server listening on {HOST}:{PORT}")
while True:
    client_socket, address = server_socket.accept()
    print(f"Connection from {address} established")
    message = client_socket.recv(1024)
    print(f"Received from client: {message}")
    response = b"Hello from the server"
    client_socket.sendall(response)
    print(f"Sent to client: {response}")
    client_socket.close()
server_socket.close()