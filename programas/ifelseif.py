def numeros(num):
    if num == 1:
        print("Tu numero es 1")
    elif num == 2:
        print("Tu numero es 2")
    elif num == 3:
        print("Tu numero es 3")
    elif num == 4:
        print("Tu numero es 4")
    else:
        print("No hay opcion")

def numeros2(num):
    if num in (1,2,3,4):
        print("Tu numero es {}".format(num))
    else:
        print("No es una opcion {}".format(num))
        
numeros(2)
numeros(4)
numeros(5)

numeros2(2)
numeros2(5)