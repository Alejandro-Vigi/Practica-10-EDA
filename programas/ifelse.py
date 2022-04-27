def obtener_mayor(param1, param2):
    if param1 < param2:
        return param2
    else:
        return param1
    
def obtener_mayor_ternario(param1,param2):
    valor = param2 if(param1 < param2) else param1
    return valor
    
print("El mayor es {}".format(obtener_mayor(4,20)))
print("El mayor es {}".format(obtener_mayor(11,6)))

print("El mayor es {}".format(obtener_mayor_ternario(4,20)))
print("El mayor es {}".format(obtener_mayor_ternario(5,6)))