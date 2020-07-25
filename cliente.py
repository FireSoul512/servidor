import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect( ('localhost',7080) ) #ip de donde se encuentra el servidor y el puerto por el que escucha

mensaje = input('Introduce el mensaje >>  ') 
s.send(bytes(mensaje, "utf-8")) #Aqui se inserta el mensaje que se envia a el server
msg = s.recv(1024) # Se obtiene la respuesta del server
print(msg.decode("utf-8")) #Se muestra la respuesta del server decodificando con utf-8
s.close() # Se cierra la connecion con el server