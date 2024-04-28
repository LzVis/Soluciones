lote = int(input("Ingrese la cantidad de lote en kilogramos "))
while lote>1:
    print(lote)
    if lote/2>1:
        lote = lote/2
    else:
        break
print(lote)