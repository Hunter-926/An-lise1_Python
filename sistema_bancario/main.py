from conta import ContaCorrente

contas = {
    '1234-5': ContaCorrente('123', '1234-5', 100.0), 
    '9876-5': ContaCorrente('111', '9876-5', 2000.0)
}

def login():
    num_conta = input('Informe seu número da conta: ')
    senha = input('Informe sua senha: ')

    conta = contas.get(num_conta)
    if conta and conta.senha == senha
        print('Seja bem vindo(a), {conta.num_conta}!')

def exibir_menu():
    print('1-Consultar saldo\n2-Depósito\n3-Transferencia\n4-Saque\n5-Sair')


while True:

    print('1-Consultar saldo\n2-Depósito\n3-Transferencia\n4-Saque\n5-Sair')
    op = int(input('Escolha uma opção: '))

    if op == 1:
        conta1.consultar_saldo()
    elif op == 2:
        valor = float(input('Escolha o valor do depósito: '))
        conta1.depositar(valor)
    elif op == 3:
        valor = float(input('Escolha o valor do transferencia: '))
        conta1.transferir(conta2, valor)
    elif op == 4:
        valor = float(input('Escolha o valor do saque: '))
        conta1.sacar(valor)
    elif op == 5:
        print('Obrigado!')
        break
    else:
        print('Opção inválida. Tente novamente.\n')

