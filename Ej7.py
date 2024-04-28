Autorizado = input("Entregue rango de autorizacion \nbajo \nmedio \nalto \nOmitir con enter para no autorizar ")
print("\n")
#Aca en caso de la variable de contener data es True y en caso de ser vacia es False
if Autorizado: 
    print("Usted esta autorizado")
    if Autorizado=="bajo":
        print("Tiene autorizacion de bajo nivel")
    if Autorizado=="medio":
        print("Tiene autorizacion de medio nivel")
    if Autorizado=="alto":
        print("Tiene autorizacion de alto nivel")
else:
    print("Usted no a sido autorizado con ningun rango")