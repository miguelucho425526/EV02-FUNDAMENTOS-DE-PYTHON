def estadisticas(numeros):
    total = sum(numeros)
    promedio = total / len(numeros)
    minimo = min(numeros)
    maximo = max(numeros)
    return total, promedio, minimo, maximo

datos = [4, 8, 15, 16, 23, 42]
suma, media, menor, mayor = estadisticas(datos)

print(f"Suma: {suma}")        
print(f"Promedio: {media}")   
print(f"Mínimo: {menor}")     
print(f"Máximo: {mayor}") 

resultado = estadisticas(datos)
print(type(resultado))  
print(resultado)        
print(resultado[1])     

"""En este caso, la función estadisticas devuelve múltiples valores, que se pueden asignar a diferentes variables."""