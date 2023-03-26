def delete():
    print('---------------------------------------------------------------')
    print('\n')
    # global linea
    # agentes = []
    # salida = []
    with open('agentes.txt', 'r') as f:
        lineas = [linea.split() for linea in f]
    for linea in lineas:
        print(linea)
    print('\n')
    ids = input('Ingrese el ID que quiera eliminar:\n')
    print('\n')
    for linea in lineas:
        if linea[0] == ids:
            lineas.remove(linea)
    for linea in lineas:
        print(linea)
    print('\n')
    print('---------------------------------------------------------------')
    print('\n')
    with open("agentes.txt", "w") as file:
        for linea in lineas:
            agente = ' '.join(str(item) for item in linea) + '\n'
            file.write(agente)
