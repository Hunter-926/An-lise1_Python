numeros = [1, 2, 3, 4, 5]
resultado = []

for numero in numeros:
    if numero % 2 == 0:
        resultado.append(numero)

print("Números pares:", resultado)