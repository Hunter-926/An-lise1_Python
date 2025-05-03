numeros = [10, 20, 30, 40, 50]
maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print("O maior número é:", maior)