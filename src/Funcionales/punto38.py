def calcular_precio_final(precio_base, descuento=0, impuesto=0.21):
    if precio_base < 0 or descuento < 0 or impuesto < 0:
        raise ValueError("Los valores no pueden ser negativos")

    precio_con_descuento = precio_base * (1 - descuento/100)
    precio_final = precio_con_descuento * (1 + impuesto)

    return precio_final

""""En este caso, la función calculará el precio final de un producto aplicando un descuento y un impuesto."""