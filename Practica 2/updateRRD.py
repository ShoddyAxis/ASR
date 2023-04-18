import time
import rrdtool
from getSNMP import consultaSNMP

multicastsend_mux = 0
paquetesRecv = 0
mensajesRespICMP = 0
segmentosSend = 0
datagramasNoEnt = 0

while 1:
    com = ''
    ip = ''
    with open('agentes.txt', 'r') as f:
        lineas = [linea.split() for linea in f]
    for linea in lineas:
        #print(linea)
        #print('\n')
        ids = linea[0]
        com = linea[1]
        ip = linea[4]
        if ids == '1':
            multicastsend_mux = int(
                consultaSNMP(com, ip,
                             '1.3.6.1.2.1.2.2.1.12.3'))
        elif ids == '4':
            multicastsend_mux = int(
                consultaSNMP(com, ip,
                             '1.3.6.1.2.1.2.2.1.12.7'))
        else:
            multicastsend_mux = int(
                consultaSNMP(com, ip,
                             '1.3.6.1.2.1.2.2.1.12.15'))
        if ids == '1':
            paquetesRecv = int(
                consultaSNMP(com, ip,
                             '1.3.6.1.2.1.2.2.1.16.3'))
        elif ids == '4':
            paquetesRecv = int(
                consultaSNMP(com, ip,
                             '1.3.6.1.2.1.2.2.1.16.7'))
        else:
            paquetesRecv = int(
                consultaSNMP(com, ip,
                             '1.3.6.1.2.1.2.2.1.16.15'))
        mensajesRespICMP = int(
            consultaSNMP(com, ip,
                         '1.3.6.1.2.1.5.22.0'))
        segmentosSend = int(
            consultaSNMP(com, ip,
                         '1.3.6.1.2.1.6.11.0'))
        datagramasNoEnt = int(
            consultaSNMP(com, ip,
                         '1.3.6.1.2.1.7.3.0'))
        valor = "N:" + str(multicastsend_mux) + ':' + str(paquetesRecv) + ':' + str(mensajesRespICMP) + ':' \
                + str(segmentosSend) + ':' + str(datagramasNoEnt)
        print(valor)
        base = "base" + ids + ".rrd"
        #print(base)
        rrdtool.update(base, valor)
    # rrdtool.dump('traficoRED.rrd','traficoRED.xml')
        time.sleep(1)

if ret:
    print(rrdtool.error())
    time.sleep(300)
