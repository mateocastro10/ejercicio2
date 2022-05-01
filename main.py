from claseManejador import ManejadorViajero
from Menu import claseMenu

if __name__ == '__main__':
    Manejador = ManejadorViajero()
    Manejador.testViajero()
    print(Manejador)
    num = int(input('Ingrese numero de viajero'))
    el = Manejador.getViajero(num)
    xmenu = claseMenu()
    b = False
    while not b:
        print('-------MENU DE OPCIONES-------')
        print(
            'opcion 1: consultar cantidad de millas \nopcion 2: acumular millas\nopcion 3: canjear millas\n opcion 4:salir')
        op = input('seleccione opcion')
        if op == 4:
            xmenu.salir()
        else:
            b = True
            if op == '1':
                xmenu.opcion1(el)
            elif op == '2':
                xmenu.opcion2(el)
            elif op == '3':
                c = int(input('Ingrese la cantidad de millas a canjear: '))
                xmenu.opcion3(c, el)
