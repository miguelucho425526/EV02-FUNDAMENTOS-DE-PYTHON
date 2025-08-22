def crear_usuario(nombre, apellido, edad, email, activo=True):
    return {
        "nombre_completo": f"{nombre} {apellido}",
        "edad": edad,
        "email": email,
        "activo": activo
    }

# Más fácil de leer con argumentos por nombre
usuario = crear_usuario(
    nombre="Juan",
    apellido="Pérez",
    edad=28,
    email="juan@ejemplo.com",
    activo=False
)

"""En este ejemplo se muestra cómo se utilizan parámetros y argumentos en una función."""