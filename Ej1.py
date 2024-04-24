#importamos la funcion sqrt de la libreria de math
from math import sqrt
#Solicitamos entradas al usuario y las almacenamos en sus respectivas variables
#Entradas eje x
x1 = int(input("Introduzca coordenada x1"))
x2 = int(input("Introduzca coordenada x2"))
x3 = int(input("Introduzca coordenada x3"))
#entradas eje y
y1 = int(input("Introduzca coordenada y1"))
y2 = int(input("Introduzca coordenada y2"))
y3 = int(input("Introduzca coordenada y3"))

#Caso de una linea descomentar lineas de codigo y comentar las de entradas
"""
x1,x2,x3= 0,0,1
y1,y2,y3 =0,0,1
"""
#Caso de un punto descomentar lineas de codigo y comentar las de entradas
"""
x1,x2,x3= 0,0,0
y1,y2,y3 =0,0,0
"""

#calculamos los lados
a = sqrt( ((x2-x1)**2) + ((y2-y1)**2) ) # pares 1 y 2
b = sqrt( ((x3-x1)**2) + ((y3-y1)**2) ) # pares 1 y 3
c = sqrt( ((x3-x2)**2) + ((y3-y2)**2) ) # pares 2 y 3


SemiPerimetro = (a + b + c)/2 #Calculamos el semi-perimetro
Area = sqrt( (SemiPerimetro * (SemiPerimetro - a) * (SemiPerimetro - b ) * (SemiPerimetro - c) )  ) #Usamos la formula de Heron y almacenamos el valor de Area


if Area == 0:
     if x1==x2==x3:
          print("Un punto no tiene Area!")
     else:
          print("Una linea no tiene Area!")
else:
     print(f"El area del triangulo es {Area}")

