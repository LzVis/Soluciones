Turno = input("Introduzca turno correspondiente ")
Edad = int(input("Introduzca la edad "))
Antiguedad = int(input("Introduzca años de antiguedad "))
DiasTrabajadosExtra = int(input("Introduzca dias trabajados extra "))

if input("escriba s para dar aprobacion ")=="s":
    Aprobacion = True
else:
    Aprobacion = False
    
    
if Edad>=18 and Edad<60:
    if Antiguedad>8:
        print("Cumple con los años de antiguedad")
    if Turno=="noche":
        Bono = 800000
    else:
        Bono = 650000
    if Aprobacion:
        print("Usted tiene la aprobacion")
    if Antiguedad>8 and Aprobacion:
        Bono = Bono + DiasTrabajadosExtra * 60000
        print(f"El bono a entregar es de {Bono}")
    else:
        print("Usted no califica")
else:
    print("Edad no permitida")