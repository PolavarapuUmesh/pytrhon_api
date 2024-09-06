import socket
HOST = 'localhost' 
PORT = 3000 
s = socket.socket()
s.bind((HOST, PORT)) 
s.listen() 
print("Server runing in port ", PORT) 
while True:
    conn, addr = s.accept() 
    res = conn.recv(1024)
    print('New conection', addr)
    print(res) 
    conn.send(b' Hello from server!')
    conn.close()