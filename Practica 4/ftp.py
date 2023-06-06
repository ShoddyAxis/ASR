from ftplib import FTP


def ftprecibe(host, user, password):
    print("*************************************************************************")
    ftp = FTP(host)
    ftp.login(user=user, passwd=password)
    nombre = input(
        "Ingrese el nombre con el que quiere identificar el archivo, el nombre generado base es: startup-config-*: ")
    print("Conexion FTP correcta")
    with open('startup-config-' + nombre, 'wb') as fp:
        ftp.retrbinary('RETR startup-config', fp.write)
        print("Archivo recibido")
    ftp.quit()
    print("Conexion FTP cerrada")


def ftpenvia(host, user, password):
    print("*************************************************************************")
    ftp = FTP(host)
    ftp.login(user=user, passwd=password)
    nombre = input("Ingrese el nombre del archivo de configuraion que quiere subir: ")
    print("Segunda conexion FTP correcta")
    ftp.storbinary('STOR startup-config', open(nombre, 'rb'))
    print("Archivo subido!")
    ftp.quit()
    print("Segunda conexion FTP cerrada")
