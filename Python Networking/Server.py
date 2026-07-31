import socket

s=socket.socket()

s.bind(("localhost",50))
s.listen(5)      #five server connection
print("Server is running.......")
s.accept()
print("Connection Established")