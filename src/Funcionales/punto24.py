def crear_lista_pares(maximo):
    return [num for num in range(2, maximo + 1, 2)]

def crear_diccionario_cuadrados(numeros):
    return {num: num ** 2 for num in numeros}

pares = crear_lista_pares(10)
print(pares) 

cuadrados = crear_diccionario_cuadrados([1, 2, 3, 4])
print(cuadrados) 

"""En este caso, las funciones crear_lista_pares y crear_diccionario_cuadrados utilizan comprensiones de listas y diccionarios para generar sus resultados de manera concisa y eficiente."""