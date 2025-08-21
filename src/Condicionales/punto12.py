fruta = input("Introduzca una fruta: ")

match fruta:
    case "manzana":
        print("La fruta es una manzana.")
    case "naranja":
        print("La fruta es una naranja.")
    case "plátano":
        print("La fruta es un plátano.")
    case _:
        print("Fruta desconocida.")

"""En este ejemplo se utiliza una estructura de coincidencia para verificar el tipo de fruta introducida y mostrar un mensaje correspondiente."""