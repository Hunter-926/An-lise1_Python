def operacao(op, a, b):
  return{
      '1': a + b,
      '2': a - b,
      '3': a * b,
      '4': a / b if b != 0 else 'Divisão por zero não aceita.'
  }.get(op, 'Operação inválida')

op = input('Escolha: 1-Soma, 2-Sub, 3-Multi, 4-Div: ')
#a,b = map(int, input('Digite dois números: ').split()) separa os valores que serão inseridos para A e B
a = int(input('Digite dois números: '))
b = int(input('Digite dois números: '))
print('Resultado: ', operacao (op, a, b))