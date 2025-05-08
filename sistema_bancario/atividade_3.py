# Criar um menu que permite ao usuário realizar N transferencias até que ele opte por sair.

while True:
  p = input('------------$------------ \nInforme o número da operação que deseja realizar? \n------------$------------ \n1-Consultar Saldo\n2-Depósito\n3-Transferencia\n4-Sair\n -----------$------------\n ')
  saldo = 5000

  if p == '1':
      print(f'Seu saldo é de: R${saldo}')
  elif p == '2':
      deposito = float(input('Informe o valor que deseja depositar: R$ '))
      saldo += deposito
      print(f'Depósito realizado com sucesso! Seu saldo atual é de: R${saldo}')
  elif p == '3':
      transferencia = float(input('Informe o valor que deseja retirar: R$ '))
      saldo -= transferencia
      if saldo < 0:
          print('Saldo insuficiente.')
      else:
          print(f'Transferencia realizado com sucesso! Seu saldo atual é de: R${saldo}')
  elif p == '4':
      print('Você saiu do sistema. Até breve!')
      break