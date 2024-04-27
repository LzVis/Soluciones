from datetime import datetime

HoraActual = datetime.now().hour
MinutoActual = datetime.now().minute
print(f"la hora es {HoraActual}:{MinutoActual}")

#Solicitamos al usuario que ingrese su nombre
nombre = input("Ingrese su nombre ") #Recordar que con input los datos ingresados son del tipo texto

#Ahora saludamos al usuario y le indicamos la hora
#Recordar que en python se hacen las salidas con print y asi estaremos imprimiendo unos datos de salida

#Aca tendriamos 4 formas para mostrar el mismo texto, preferentemente es mas sencilla la primera.
print(f"Bienvenid@ {nombre}, son las {HoraActual}:{MinutoActual}")
print("Bienvenid@ {0}, son las {1}:{2}".format(nombre,HoraActual,MinutoActual))
print("Bienvenid@ "+str(nombre)+" son las "+str(HoraActual)+":"+str(MinutoActual))
print("Bienvenid@",nombre,"son las ",HoraActual,":",MinutoActual)