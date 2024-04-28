palabra = input("ingrese una palabra") #Solicitamos al usuario una palabra cualquiera
vocales = "aeiou" #Escribimos las vocales 
for vocal in vocales: #Aca realizamos una iteracion a vocales y con la variable vocal en cada ciclo tomara los valores de vocales
    #print(vocal) #Con este print podemos corroborar los valores que toma vocal en el ciclo for
    if vocal in palabra: #Consultamos si vocal se encuentra dentro de palabra usando el operador in
        print(f"la vocal {vocal} se encuentra en la palabra {palabra}")