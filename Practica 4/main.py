from telnet import cliente
from ftp import ftprecibe
from ftp import ftpenvia

menu = 0
while 1:
    print("Que es lo que desea hacer? \n "
          "\t1.-Generar la configuracion de un dispositivo de manera remota \n"
          "\t2.-Extraer el archivo de configuracion\n"
          "\t3.-Importar el archivo configuracion")
    menu = input("Seleccione la opcion deseada : ")
    if menu == '1':
        host = input("\tIngrese la direccion del host: ")
        usuario = input("\tIngrese el usuario: ")
        password = input("\tIngrese la contrasena: ")
        cliente(host, usuario, password)
        print("*************************************************************************")
    if menu == '2':
        host = input("\tIngrese la direccion del host: ")
        usuario = input("\tIngrese el usuario: ")
        password = input("\tIngrese la contrasena: ")
        ftprecibe(host, usuario, password)
        print("*************************************************************************")
    if menu == '3':
        host = input("\tIngrese la direccion del host: ")
        usuario = input("\tIngrese el usuario: ")
        password = input("\tIngrese la contrasena: ")
        ftpenvia(host, usuario, password)
        print("*************************************************************************")

