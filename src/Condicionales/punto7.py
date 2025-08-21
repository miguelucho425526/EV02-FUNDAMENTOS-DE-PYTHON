saldo = 300
retiro = 500
if saldo >= retiro:
    saldo -= retiro
    print("Retiro exitoso.")
    print(f"Nuevo saldo: {saldo}")
else:
    print("Fondos insuficientes.")
    print(f"Saldo actual: {saldo}")

"""En este ejemplo se utiliza una estructura condicional para verificar si hay suficientes fondos para realizar un retiro y actualizar el saldo en consecuencia."""