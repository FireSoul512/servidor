import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind( ('localhost',7080) )
s.listen(5)
ciclo = True
print('Para cerrar el server el cliente tiene que introducir SALIR')

while ciclo:
    conexion, addr = s.accept()
    print("Nueva conexion",addr)
    print(addr)
    conexion.send(bytes("Hola como estas", "utf-8"))
    msg = conexion.recv(1024)
    print(msg.decode("utf-8"))
    conexion.close()
    if msg.decode("utf-8") == "SALIR":
        ciclo = False

print('Adios bro XD')