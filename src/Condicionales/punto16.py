numeros = [1, 2, 3, 4]

match numeros:
    case []:
        print("La lista está vacía.")
    case [uno]:
        print(f"Un solo elemento: {uno}.")
    case [uno, dos]:
        print(f"Dos elementos: {uno} y {dos}.")
    case [uno, *resto]:
        print(f"Primer elemento: {uno}, resto de la lista: {resto}.")

"""En este ejemplo se utiliza una estructura de coincidencia para verificar el contenido de una lista y mostrar información sobre sus elementos."""