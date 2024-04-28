tiempo = float(input("ingrese el tiempo en segundos ")) #Aca establecemos que la variable ingresada sea del tipo flotante(decimal) con  float(valor)
DatoACalcular = input("Escriba el dato que desee calcular. \naltura \nvelocidad final\n")
if DatoACalcular=="velocidad final": #Mediante la sentencia if le preguntamos si la declaracion es True y en caso de ser True, ejecutara lo que esta indexado 
    velocidadFinal = 9.81*tiempo
    print(f"la velocidad final es {velocidadFinal} metros por segundo")
#Mediante la sentencia elif lo que hacemos es que en caso de que sea false el if el programa pregunte si la sentencia dentro del elif es True, y en caso de ser ejecutara lo que esta indexado 
elif DatoACalcular=="altura": 
    altura = ((tiempo**2)*9.81)/2
    print(f"la altura es {altura} metros")
#Con la sentencia else lo que hacemos es que ya como ultima opcion ejecute lo que tiene indexado el else
#Como es la ultima opcion observar que no evalua si es false o true.
else:
    print("no se selecciono ninguna de las 2 opciones ejecute nuevamente")
    
    