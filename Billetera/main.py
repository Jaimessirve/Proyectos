from graficos import *

print("\t\t****BILLETERA CMD****")
archivo = open("texto.txt", "r")
linea = archivo.readline()
while linea != "":
    linea = archivo.readline()
    print(linea)
graficos()