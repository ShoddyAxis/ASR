from getSNMP import consultaSNMP
from pdf import repagn


def getdata():
    print('---------------------------------------------------------------')
    print('\n')
    infst = []
    infdc = []
    com = ''
    ip = ''
    with open('agentes.txt', 'r') as f:
        lineas = [linea.split() for linea in f]
    for linea in lineas:
        print(linea)
    print('\n')
    ids = input('Ingrese el ID que quiera generar la consulta:\n')
    print('\n')
    for linea in lineas:
        if linea[0] == ids:
            com = linea[1]
            ip = linea[4]
    """ print(com)
    print(ip)"""
    so = str(
        consultaSNMP(com, ip, '1.3.6.1.2.1.1.1.0'))
    nomd = str(
        consultaSNMP(com, ip, '1.3.6.1.2.1.1.5.0'))
    coif = str(
        consultaSNMP(com, ip, '1.3.6.1.2.1.1.4.0'))
    ub = str(
        consultaSNMP(com, ip, '1.3.6.1.2.1.1.6.0'))
    nmif = int(
        consultaSNMP(com, ip, '1.3.6.1.2.1.2.1.0'))
    ns = nmif+1
    for nmif in range(1,ns):
        con1 = '1.3.6.1.2.1.2.2.1.2.'+ str(nmif)
        con = '1.3.6.1.2.1.2.2.1.8.'+ str(nmif)
        infs1 = str(
            consultaSNMP(com, ip, con1)
        )
        infdc.append(infs1)
        infss= int(
            consultaSNMP(com, ip, con))
        if infss == 1:
            infst.append('UP')
        if infss == 2:
            infst.append('DOWN')
        if infss == 3:
            infst.append('TESTING')
    print("Sistema Operativo =", so, '\n')
    print("Nombre del dispositivo =", nomd, '\n')
    print("Informacion de contacto ", coif, '\n')
    print("Ubicacion =", ub, '\n')
    print("Numero de Interfaces =", nmif,'\n')
    ni = 1
    for inf in infdc:
        print('La descripcion de la interfaz#' + str(ni) + ' es ' + inf)
        ni+=1
        print('\n')
    ni=1
    for inf in infst:
        print('El estado interfaz #'+ str(ni) + " es "+inf +'\n')
        ni+=1
        print('\n')
    print('---------------------------------------------------------------')
    print('\n')
    # for ins in infs:
    # print(ins)
    repagn(ids,so,nomd,coif,ub,nmif,infdc,infst)