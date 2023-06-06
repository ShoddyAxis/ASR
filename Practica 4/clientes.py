from ftplib import FTP
import telnetlib

HOST = "192.168.1.1"  # Router 1
HOST2 = "192.168.1.2"  # Router 2
user = "rcp"
password = "rcp"

#print("Que es lo que desea hacer? \n \t 1.- Modificar ")

tn = telnetlib.Telnet(HOST)
tn.read_until(b"User: ")
tn.write(user.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")
xd = input("Instruccion: ")
print(xd.encode('ascii'))
print("Conexion correcta!")
tn.read_until(b">")
tn.write(b"en\n")
print("Habilitado")
tn.read_until(b"#")
tn.write(b"conf\n")
print("Listo para configurar")
tn.read_until(b"#")
tn.write(xd.encode('ascii') + b"\n")
#tn.write(b"hostname R1\n")
print("Nombre cambiado")
tn.read_until(b"#")
tn.write(b"copy run start\n")
print("Persistencia iniciada")
tn.read_until(b"#")
tn.write(b"exit\n")
print("Conexion cerrada")
tn.close()
