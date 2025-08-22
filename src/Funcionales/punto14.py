def sumar(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(sumar(1, 2))  
print(sumar(1, 2, 3, 4, 5))  
print(sumar())  

"""En este ejemplo se muestra cómo se utilizan parámetros y argumentos en una función."""