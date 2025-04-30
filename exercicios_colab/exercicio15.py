op = input('Digite um dia da semana: ')
print({
      '1': 'Segunda',
      '2': 'Terça',
      '3': 'Quarta',
      '4': 'Quinta',
      '5': 'Sexta',
      '6': 'Sábado',
      '7': 'Domingo'
  }.get(op, 'Opção inválida'))