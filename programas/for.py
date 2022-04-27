import enum


for x in [1,2,3,4,5]:
    print(x)

for x in range(5): #[0, 5)
    print(x)
    
for x in range (-5,2): #[-5, 1]
    print(x)
    
for x in ["uno", "dos", "tres", "cuatro"]:
    print(x)

elementos = {'hidrogeno':1, 'helio':2, 'carbono':6}
for key, value in elementos.items():
    print(key, "=", value)
    
for key in elementos.keys():
    print(key)
    
for value in elementos.values():
    print(value)
    
for idx, x in enumerate(elementos):
    print("El indice es: {} y el elemento {}".format(idx, x))
    
def cuenta1(limite):
    for i in range(limite, 0, -1):
        print(i)
    else:
        print("Cuenta terminada")
        
cuenta1(8)

def cuenta2(limite):
    for i in range(limite,0,-1):
        print(i)
        if i==3:
            break
    else:
        print("Cuenta terminada")
        
cuenta2(8)
cuenta2(2)