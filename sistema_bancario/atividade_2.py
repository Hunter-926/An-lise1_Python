# Criar uma segunda conta corrente, para simular saque,depósito e transferência.

p = input('Informe o número da operação que deseja realizar?\n1-Consultar Saldo\n2-Depósito\n3-Transferencia\n ')
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