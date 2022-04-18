import csv
from mail import Email
import os

def test () :
    print('------ TEST ------')
    print('datos a probar: \nDatos correctos: \ninformatica.fcefn@gmail.com, píchi23@hotmail.com, juanLiendro1957@yahoo.com \n\nDatos incorrectos: \nmaltiyopmail.com, jorfeaste@tinymail')
    nuevotest= Email()
    print('\n\n-------DATOS CORRECTOS-------')
    print('informatica.fcefn@gmail.com')
    nuevotest.crearcuenta('informatica.fcefn@gmail.com','pw1')
    print('píchi23@hotmail.com')
    nuevotest.crearcuenta('píchi23@hotmail.com','pw2')
    print('juanLiendro1957@yahoo.com')
    nuevotest.crearcuenta('juanLiendro1957@yahoo.com','pw3')
    print('\n--- DATOS INCORRECTOS')
    print('maltiyopmail.com')
    nuevotest.crearcuenta('maltiyopmail.com','pw4')
    print('jorfeaste@tinymail')
    nuevotest.crearcuenta('jorfeaste@tinymail','pw5')
    os.system('Pause')
    os.system('cls')


if __name__=='__main__':
 i = input("ingrese id cuenta")
 d = input("ingrese dominio")
 t = input("ingrese tipo de dominio")
 c = input("ingrese contraseña")
 nombre = input("ingrese su nombre")
 unMail = Email(i,d,t,c)
 print("Estimado",nombre,"le enviaremos los mensajes a su cuenta",(unMail.retornaEmail()))
 unMail.getDominio()
 unMail.modifica()
 mail = input("ingrese correo")
 otroMail = Email()
 otroMail.crearcuenta(mail)
