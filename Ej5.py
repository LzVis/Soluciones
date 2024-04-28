DiaDeSemana = int(input("ingrese el numero de semana ")) #Solicitamos al usuario que ingrese un numero el cual le correspondera a un dia de la semana
#Usamos un if para iniciar con los condicionales
if DiaDeSemana == 1:
    print("Lunes")
#Aca empezamos usando un elif en caso de que no se cumpla la condicion de arriba
elif DiaDeSemana == 2:
    print("Martes")
elif DiaDeSemana == 3:
    print("Miercoles")
elif DiaDeSemana == 4:
    print("Jueves")
elif DiaDeSemana == 5:
    print("Viernes")
elif DiaDeSemana == 6:
    print("Sabado")
elif DiaDeSemana == 7:
    print("Domingo")
#Ya por ultimo usamos un else, debido que si ninguno de los casos arriba sucede que se ejecute el codigo del else
else:
    print("No coicide con ningun dia")