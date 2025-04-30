op = input('Digite um número de 1 a 5: ')
print({
      '1': 'um',
      '2': 'dois',
      '3': 'três',
      '4': 'quatro',
      '5': 'cinco'
  }.get(op, 'Opção inválida'))