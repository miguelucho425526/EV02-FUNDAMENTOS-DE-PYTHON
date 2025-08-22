def generar_contraseña(longitud=8):
    import random
    import string
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

"""En este caso, la función generará una contraseña aleatoria de la longitud especificada."""