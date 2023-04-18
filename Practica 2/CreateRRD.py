#!/usr/bin/env python
import rrdtool

with open('agentes.txt', 'r') as f:
    lineas = [linea.split() for linea in f]
for linea in lineas:
    # print(linea)
    # print('\n')
    ids = linea[0]
    name = "base" + ids + ".rrd"
    ret = rrdtool.create(name,
                     "--start", 'N',
                     "--step", '30',
                     "DS:paquetesSendMux:COUNTER:120:U:U",
                     "DS:paquetesRecv:COUNTER:120:U:U",
                     "DS:mensajesRespICMP:COUNTER:120:U:U",
                     "DS:segmentosSend:COUNTER:120:U:U",
                     "DS:datagramasNoEnt:COUNTER:120:U:U",
                     "RRA:AVERAGE:0.5:1:300",
                     "RRA:AVERAGE:0.5:1:300",
                     "RRA:AVERAGE:0.5:1:300",
                     "RRA:AVERAGE:0.5:1:300",
                     "RRA:AVERAGE:0.5:1:300")
    if ret:
        print(rrdtool.error())
