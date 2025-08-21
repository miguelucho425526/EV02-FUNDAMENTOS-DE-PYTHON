usuarios = [
    {"nombre": "Ana", "rol": "admin"},
    {"nombre": "Luis", "rol": "usuario"},
    {"nombre": "Marta", "rol": "moderador"}
]

for usuario in usuarios:
    match usuario:
        case {"rol": "admin"}:
            print(f"{usuario['nombre']} tiene permisos de administrador.")
        case {"rol": "moderador"}:
            print(f"{usuario['nombre']} puede moderar contenidos.")
        case {"rol": "usuario"}:
            print(f"{usuario['nombre']} es un usuario regular.")
        case _:
            print(f"Rol de {usuario['nombre']} desconocido.")

"""En este ejemplo se utiliza una estructura de coincidencia para verificar el rol de un usuario y mostrar un mensaje correspondiente."""