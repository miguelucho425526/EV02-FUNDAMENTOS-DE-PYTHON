def dividir_seguro(a, b):

    if b == 0:
        print("Error: División por cero")
        return None
    
    resultado = a / b
    return resultado

print(dividir_seguro(10, 2))   
print(dividir_seguro(10, 0)) 

"""En este caso, la función dividir_seguro maneja la división por cero de manera segura, evitando errores en tiempo de ejecución."""