def formato_nombre(nombre, apellido):
    return f"{apellido.upper()}, {nombre.capitalize()}"

print(formato_nombre("ana", "garcía"))

"""En este caso, la función formato_nombre devuelve una cadena con el apellido en mayúsculas y el nombre capitalizado."""