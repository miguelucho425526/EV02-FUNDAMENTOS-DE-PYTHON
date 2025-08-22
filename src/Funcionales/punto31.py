def validar_email(email):
    if not isinstance(email, str):
        raise TypeError("El email debe ser una cadena de texto")
    return "@" in email and "." in email.split("@")[-1]

"""Esta función valida el formato de un correo electrónico."""