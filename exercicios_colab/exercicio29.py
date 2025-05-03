palavra = str(input("Digite uma palavra: "))
vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

print("Letras escolhidas: ")
for letra in palavra:
    if letra in vogais:
        print(letra)