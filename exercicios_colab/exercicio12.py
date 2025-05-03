def converter(op, t):
  return{
      '1': (t*9/5)+32,
      '2': t+273.15,
      '3': (5/9)*(t-32),
      '4': t*1.8-459.67,
      '5': t+273.15,
      '6': (t-273.15)*1.8+32
  }.get(op, 'Opção inválida')

op = input('Digite a conversão desejada: 1-Cel./Fah., 2-Cel./Kel., 3-Fah./Cel., 4-Fah./Kel., 5-Kel./Cel., 6-Kel./Fah.: ')
t = float(input('Digite a temperatura de acordo com o valor selecionado acima: '))
print('Temperatura convertida: ', converter(op, t))