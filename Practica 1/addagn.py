def agenteadd(nid):
    print('---------------------------------------------------------------')
    print('\n')
    ids = str(nid)
    cm = input('Cual es el nombre de la comunidad? \n')
    print('\n')
    prt = input('Cual es el puerto? \n')
    print('\n')
    vsn = input('Cual es la version SNMP? \n')
    print('\n')
    ips = input('Cual es la direccion ip? \n')
    print('\n')
    with open("agentes.txt", "a") as file:
        file.write(ids + " " + cm + " " + prt + " " + vsn + " " + ips + "\n")
    print('---------------------------------------------------------------')
    print('\n')
def agenteedit(nid):
    print('---------------------------------------------------------------')
    print('\n')
    ids = str(nid)
    cm = input('Cual es el nombre de la comunidad? \n')
    print('\n')
    prt = input('Cual es el puerto? \n')
    print('\n')
    vsn = input('Cual es la version SNMP? \n')
    print('\n')
    ips = input('Cual es la direccion ip? \n')
    print('\n')
    agen = [ids, cm, prt, vsn, ips]
    print('---------------------------------------------------------------')
    print('\n')
    return agen
    
