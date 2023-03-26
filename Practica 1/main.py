from addagn import agenteadd
from dfid import numid
from deleteagn import delete
from mod import edit
from updateSNMP import getdata


menu = 0
while 1:
    print(' Agregar un Agente || #1 \n')
    print(' Editar un Agente || #2 \n')
    print(' Eliminar un Agente || #3 \n')
    print(' Generar el reporte de un Agente || #4 \n')
    print(' Salir || #5 \n')
    menu = input('Seleccione la opcion deseada \n')
    print('\n')
    print('---------------------------------------------------------------')
    if menu == '1':
        cont = numid() + 1
        agenteadd(cont)
    if menu == '2':
        edit()
    if menu == '3':
        delete()
    if menu == '4':
        getdata()
    if menu == '5':
        quit()

