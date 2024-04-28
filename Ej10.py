MetrosCuadrados = int(input("Introduzca cantidad de metros cuadrados del proyecto "))
Costo = 1.7
Profundidad = int(input("Introduzca la profundidas de la operacion "))

if Profundidad>10:
    Costo = Costo *1.5
elif Profundidad>20:
    Costo = Costo *2
elif Profundidad>30:
    Costo = Costo *2.2
elif Profundidad>40:
    Costo = Costo *2.2

Presupuesto = Costo * MetrosCuadrados

if Presupuesto>100:
    print("presupuesto no aprobado")
else:
    print("presupuesto aprobado")