import socket

s = socket.socket()

s.connect(("localhost", 5000))

data = s.recv(1024)
print(data.decode())

s.close()