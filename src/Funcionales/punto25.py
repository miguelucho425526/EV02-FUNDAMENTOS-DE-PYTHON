# Enfoque mejorado: siempre devuelve una lista (vacía en caso de error)
def filtrar_positivos(numeros):
    if not isinstance(numeros, list):
        return []  # Lista vacía en caso de error

    return [num for num in numeros if num > 0]

"""En este caso, la función filtrar_positivos devuelve una lista con los números positivos de la lista original, o una lista vacía si la entrada no es válida."""