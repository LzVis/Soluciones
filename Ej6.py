lote = int(input("Ingrese la cantidad de lote en kilogramos "))
conteo = 0
while lote>1:
    print(f"la cantidad del lote es {lote} y van en el cuarteo numero {conteo}")
    conteo+=1
    if lote/2>=1:
        lote = lote/2
    else:
        break