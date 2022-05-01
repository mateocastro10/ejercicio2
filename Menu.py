
class claseMenu:
    __op=0
    def __init__(self):
        self.__op=None
    def opcion(self,op):
        if op=='1':
            self.opcion1()
        elif op=='2':
            self.opcion2()
        elif op=='3':
            self.opcion3()
    def salir(self):
        print('Usted salio del programa')


    def opcion1(self, el):
        print('Cantidad total de millas: ', el.cantidadTotalMillas())


    def opcion2(self, el):
        millas = int(input('Ingrese cant'))
        print('Valor actualizado de las millas acumuladas: ', el.acumularmillas(millas))

    def opcion3(self, c, el):
        el.canjear(c)
