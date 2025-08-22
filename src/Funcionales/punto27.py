def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

notas = [7, 8, 6, 9]
promedio = calcular_promedio(notas)
print(f"El promedio es: {promedio}")

"""En este caso, la función calcular_promedio permite calcular el promedio de una lista de números de manera sencilla y reutilizable."""