import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind( ('localhost',8000) )
s.listen(5)

while True:
    conexion, addr = s.accept()
    print("Nueva conexion")
    print(addr)
    conexion.send(bytes("Hola como estas", "utf-8"))
    msg = conexion.recv(1024)
    print(msg.decode("utf-8"))
    conexion.close()