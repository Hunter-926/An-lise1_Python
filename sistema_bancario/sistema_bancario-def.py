conta1 = '1234'
saldo1 = 100.0

conta2 = '7894'
saldo2 = 2000.0


#-------------------------------------------------------------------------------------

def exibir_menu():
    print('1-Consultar saldo\n2-Depósito\n3-Transferencia\n4-Saque\n5-Sair')

def sacar(valor):
    global saldo
    saldo -= valor 
    print(f"O saldo atual da conta: {saldo}")

def depositar(valor):
    global saldo
    saldo += valor 
    print(f"O saldo atual da conta: {saldo}")

def transferir(valor):
    global saldo, destinatario
    saldo -= valor 
    destinatario += valor
    print(f"O saldo atual da conta: {saldo}")

while True:

    print('1-Consultar saldo\n2-Depósito\n3-Transferencia\n4-Saque\n5-Sair')
    op = int(input('Escolha uma opção: '))

    if op == 1:
        print(f'O saldo da conta 1: {saldo1}')
    elif op == 2:
        valor = float(input('Escolha o valor do depósito: '))
        depositar(valor)
    elif op == 3:
        valor = float(input('Escolha o valor do transferencia: '))
        transferir(valor)
    elif op == 4:
        valor = float(input('Escolha o valor do saque: '))
        sacar(valor)
    elif op == 5:
        print('Obrigado!')
    break

