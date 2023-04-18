import re

from pysnmp.hlapi import *


def hex_to_string(hex):
    if hex[:2] == '0x':
        hex = hex[2:]
    string_value = bytes.fromhex(hex).decode('utf-8')
    return string_value


def consultaSNMP(comunidad, host, oid):
    errorStatus, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(comunidad),
               UdpTransportTarget((host, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(oid))))

    if errorStatus:
        print(errorStatus)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            varB = (' = '.join([x.prettyPrint() for x in varBind]))
            resultado = varB.split()[2]
            if oid == '1.3.6.1.2.1.1.1.0':
                if resultado == 'Linux':
                    resultado = varB.split()[5]
                    nu = re.findall('[A-Za-z]', resultado)
                    resultado = "".join(nu)
                if resultado == 'Hardware:':
                    resultado = varB.split()[14]
                    nu = re.findall('[A-Za-z]', resultado)
                    resultado = "".join(nu)
            if '0x' in resultado:
                resultado = hex_to_string(resultado)


    return resultado