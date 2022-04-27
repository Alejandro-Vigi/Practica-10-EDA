def cuenta(limite):
    i = limite
    while True:
        print(i)
        i = i-1
        if i == 0:
            break

cuenta(10)

def factorial(n):
    i = 2
    fact = 1
    while i <= n:
        fact = fact * i
        i = i + 1
    return fact

print("EL factorial de 4 es {}".format(factorial(4)))
print("EL factorial de 1 es {}".format(factorial(1)))
print("EL factorial de 5 es {}".format(factorial(5)))
print("EL factorial de 0 es {}".format(factorial(0)))