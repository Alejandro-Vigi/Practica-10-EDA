def obtener_mas_grande(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
        
print("El mas grande es {}".format(obtener_mas_grande(7,13,1)))