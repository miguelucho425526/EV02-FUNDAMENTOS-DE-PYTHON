def es_mayor_de_edad(edad):
    return edad >= 18

def es_correo_valido(email):
    return "@" in email and "." in email

usuario_edad = 16
if es_mayor_de_edad(usuario_edad):
    print("Acceso permitido")
else:
    print("Acceso denegado") 

"""En este caso, las funciones es_mayor_de_edad y es_correo_valido encapsulan la lógica de validación, lo que hace que el código sea más limpio y fácil de mantener."""

