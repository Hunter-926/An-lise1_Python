
saldo -= valor 

saldo += valor 

saldo1 -= valor
saldo2 += valor 


conta1 = '1234'
saldo1 = 100.0

conta2 = '7894'
saldo2 = 2000.0

while True:
    print('1-Consultar saldo\n2-Depósito\n3-Transferencia\n4-Saque\n5-Sair')
    op = int(input('Escolha uma opção: '))

    if op == 1:
        print(f'O saldo da conta 1: {saldo1}')
    elif op == 2:
        valor = float(input('Escolha o valor do depósito: '))
        saldo1 += valor 
        print(f'O saldo atual da conta 1: {saldo1}')
    elif op == 3:
        saldo1 -= valor
        saldo2 += valor
        valor = float(input('Escolha o valor do transferencia: '))
        print(f'O saldo atual da conta 1: {saldo1}')
    elif op == 4:
        valor = float(input('Escolha o valor do saque: '))
        saldo1 -= valor 
        print(f'O saldo atual da conta 1: {saldo1}')
    elif op == 5:
        print('Obrigado!')
    break

#-----------------------------------------------------------------------------

