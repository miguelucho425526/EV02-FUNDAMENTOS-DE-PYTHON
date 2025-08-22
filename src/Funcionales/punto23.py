def calcular_precio_con_iva(precio_base, tasa_iva=0.21):
    return precio_base * (1 + tasa_iva)

precio_final = calcular_precio_con_iva(100)
print(f"Precio con IVA: {precio_final} €")

"""En este caso, la función calcular_precio_con_iva permite calcular el precio de un producto incluyendo el IVA de manera sencilla y reutilizable."""