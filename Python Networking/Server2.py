import socket

s = socket.socket()

s.bind(("localhost", 5000))
s.listen(10)

print("Server is running...")

conn, addr = s.accept()
print("Connected:", addr)

conn.send(b"Hello Client")

conn.close()
s.close()