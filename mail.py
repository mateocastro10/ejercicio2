class Email:

    def __init__(self, i, d, t, c):
        self.__idcuenta = i
        self.__dominio= d
        self.__tipodominio = t
        self.__contraseña = c

    def retornaEmail(self):
        return (self.__idcuenta +'@'+ self.__dominio +'.'+ self.__tipoDominio)

    def getDominio(self):
            return(self.__dominio)

    def crearcuenta(self,mail):
        if (mail.find('@')!= -1):
            xc= mail.split('@')
            idnuevo= xc[0]
            if (xc[1].find('.')!= -1):
                dc= xc[1].split('.')
                xd= dc[0]
                xtd= dc[1]
                self.__init__(idnuevo,xd,xtd,c)
                print('Correo creado con exito')
            else: print('Error: El dominio no contiene punto')
        else: print ('Error: El correo ingresado no contiene @')

    def modifica(self):
        x = input("ingrese contraseña actual")
        while(x != self.__contraseña):
            print("contraseña incorrecta")
        else:
             self.__contraseña = input("ingrese nueva contraseña")
