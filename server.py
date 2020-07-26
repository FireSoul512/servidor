import socket #Librerias del socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind( ('localhost',7080) ) #IP del server y puerto donde se hace la conneccion
s.listen(5) #Numero de connecciones maximas permitidas
ciclo = True
print('Para cerrar el server el cliente tiene que introducir SALIR')

while ciclo: #Ciclo infinito, pero le puse que se cerrara cuando el cliente enviara "SALIR"
    conexion, addr = s.accept() #Aqui el server queda a espera para resibir una coneccion
    print("Nueva conexion",addr) #Muestra la ip y el puerto el cual esta el cliente
    conexion.send(bytes("Hola como estas", "utf-8")) #De esta forma el server puede regresar un mensaje
    msg = conexion.recv(1024) # De esta forma se obtiene el mensaje que envio el cliente
    print(msg.decode("utf-8")) # Aqui se decodifica en utf-8
    conexion.close() # Se cierra la conexion con el cliente
    if msg.decode("utf-8") == "SALIR": # Validacion para cerrar el server usando el mensaje del cliente
        ciclo = False

print('Adios bro XD')
s.close()