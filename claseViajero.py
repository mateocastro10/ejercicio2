class Viajero:
    __dni = 0
    __num_viajero = 0
    __nombre = ''
    __apellido = ''
    __millas_acum = 0

    def __init__(self, nv, dni, nom, ape, ma):
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = ape
        self.__num_viajero = nv
        self.__millas_acum = ma

    def cantidadTotalMillas(self):
        cant1 = self.__millas_acum
        return cant1

    def acumularmillas(self, millas):
        if(type(millas)==int):
            valor1 = self.__millas_acum + millas
            return valor1
        else:
            print('TIPO DE DATO INCORRECTO')

    def canjear(self, c):
        if(type(c)==int):
            if c <= self.__millas_acum:
                valor2 = self.__millas_acum - c
                print('Valor actualizado de las millas acumuladas: ', valor2)
            else:
                print("ERROR, MILLAS INSUFICIENTES")
        else:
            print('TIPO DE DATO INCORRECTO')
