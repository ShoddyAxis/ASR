ids = []


def numid():
    idi = 0
    with open('agentes.txt', 'r') as f:
        lineas = [linea.split() for linea in f]
    for linea in lineas:
        # print(linea)
        ids.append(int(linea[0]))
    if len(ids) == 0:
        return 0
    else:
        idi = mayor(ids)
    return idi


def mayor(idn):
    ma = ids[0]
    for n in ids:
        if n > ma:
            ma = n
    print(ma)
    return ma
