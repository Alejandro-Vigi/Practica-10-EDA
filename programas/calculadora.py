def menu():
    print("Selecciona una operacion")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicacion")
    print("4.- Division")
    print("5.- Salir")
    opcion = int(input())
    return opcion

def calculadora():
    op = menu()
    num1 = int(input("Ingresa el primer operando: "))
    num2 = int(input("Ingresa el segundo operando: "))
    if op == 1:
        print(num1+num2)
    elif op == 2:
        print(num1-num2)
    elif op == 3:
        print(num1*num2)
    elif op == 4:
        print(num1/num2)
    else:
        print("Adios")
        
calculadora()
    