import socket 
Host="localhost"
port=3000
s=socket.socket()
s.connect(Host,port)
s.send(b"Hello from the client")
res=s.recv(1024)
print(res)
s.close