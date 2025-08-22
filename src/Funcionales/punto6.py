def calcular_precio_final(precio_base, impuesto):
    return precio_base + (precio_base * impuesto)

total = calcular_precio_final(100, 0.21)
print(f"Precio final: {total}")  

"""En este ejemplo se muestra cómo se utilizan funciones para realizar cálculos y devolver resultados."""
