import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect( ('189.148.85.231',8000) )

s.send(bytes("si", "utf-8"))
msg = s.recv(1024)
print(msg.decode("utf-8"))
s.close()