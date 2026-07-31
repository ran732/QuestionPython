import socket

s=socket.socket()
s.connect(("localhost",247))
expr=input("Enter Expression :")
s.send(expr.encode())
b=s.recv(2048)
print(b.decode())