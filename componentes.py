from os import replace
from helpers import borrarPantalla, gotoxy
from crudArhivos import Archivo
import time
from datetime import datetime
class Menu:
    def __init__(self,titulo="",opciones=[],col=6,fil=1):
        self.titulo=titulo
        self.opciones=opciones
        self.col=col
        self.fil=fil
        
    def menu(self):
        gotoxy(self.col,self.fil);print(self.titulo)
        self.col-=5
        for opcion in self.opciones:
            self.fil +=1
            gotoxy(self.col,self.fil);print(opcion)
        gotoxy(self.col+5,self.fil+2)
        opc = input("Elija opcion[1...{}]:".format(len(self.opciones))) 
        return opc   
class Valida:
    def solo_numeros(self,mensajeError,col,fil):
        while True: 
            gotoxy(col,fil)            
            valor = input()
            try:
                if int(valor) > 0:
                    break
            except:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*20)
        return valor

    def solo_letras(self,mensaje,mensajeError): 
        while True:
            valor = str(input("          ------>   | {} ".format(mensaje)))
            if valor.isalpha():
                break
            else:
                print("          ------><  | {} ".format(mensajeError))
        return valor

    def solo_decimales(self,mensajeError,col,fil):
        while True:
            gotoxy(col,fil)
            valor = str(input())
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*20)
        return valor
    def telefono(self,mensajeError,col,fil):
        
        while True:
            gotoxy(col,fil)
            valor = str(input())
            if valor.isdigit()and len(valor)==10 or len(valor)==12:
                break
            else:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*len(mensajeError))
        return valor
    
    def solo_letrass(self,mensajeError,col,fil): 
        while True:
            gotoxy(col,fil)
            valor = str(input().upper())
            if valor.isalpha():
                break
            else:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*len(mensajeError))
        return valor
    def ruc(self,mensajeError,col,fil):
        while True:
            gotoxy(col,fil)
            codigoprovincial1=["0","1","2"]
            codigoprovincial2=["1","2","3","4"]
            valor = str(input())
            if valor.isdigit()and len(valor)==10 and valor[0]in codigoprovincial1 and valor[1]in codigoprovincial2:
                break 
            else:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*len(mensajeError))
        return valor+"-001"
    def fechas(self,mensajeError,col,fil):
        while True:
            gotoxy (col,fil)
            tipo="0000-01-01"
            fechaa=input()
            if fechaa.isdigit and len(fechaa)==len(tipo) and fechaa[4]==tipo[4] and fechaa[7]==tipo[7]:
                break
            else:
                gotoxy(col,fil);print(tipo)
                gotoxy(col+20,fil);print("Ingrese formato correcto")
                time.sleep(1)
        return fechaa
    def cargoydepar(self,mensajeError,col,fil): 
        while True:
            gotoxy(col,fil)
            valor = input()
            if valor.isalpha():
                break
            else:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*len(mensajeError))   
    def periodo(self,mensajeError,col,fil):
        while True:
            gotoxy (col,fil)
            tipo="aaaamm"
            vp=input()
            if vp.isdigit() and len(vp)==len(tipo) and vp[0]=="2" and vp[1]=="0":
                break
            else:
                gotoxy(col,fil);print(tipo+"]"," "*20)
                gotoxy(col+20,fil);print(mensajeError)
                time.sleep(1)               
        return vp
    def vroles(self,mensajeError,col,fila):
        pass