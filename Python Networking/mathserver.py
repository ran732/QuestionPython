import socket

s=socket.socket()

s.bind(("localhost",247))

s.listen(10)

print("MAth server is running.")

while True:
    t=s.accept()
    c=t[0]
    b=c.recv(2048)
    expr=b.decode()
    res=eval(expr)
    result=f'Result is {res}'
    c.send(result.encode())