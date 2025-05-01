numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero % 2 == 0:
        numeros.append(numero)

print("Números pares digitados:", numeros)