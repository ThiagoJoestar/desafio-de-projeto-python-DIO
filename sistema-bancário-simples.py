print('Bem vindo ao Banco DIO!')
menu = '''
=======================
MENU DE OPÇÕES:
[D] Depositar
[S] Sacar
[E] Extrato
[F] Finalizar
=======================
SELECIONE A OPÇÃO DESEJADA: '''

saldo = numero_saques = valor_saque= deposito = 0
 
while True:
    option = input(menu).upper().split()[0]
    
    if option == 'D':
        print('DEPOSITO')
        deposito = int(input('Valor a ser depositado: R$'))
        saldo += deposito
        print(f'Saldo atual R${saldo:.2f}')
    
    elif option == 'S':
        if numero_saques > 3:
            print('Você atigiu o limite de saques por dia!')
            break    
        print('SAQUE')
        print(f'Saldo atual R${saldo:.2f}')
        valor_saque = int(input('Digite o valor que deseja retirar: R$ '))
        numero_saques += 1
        if saldo < valor_saque:
            print('Saldo insulficiente!')
        elif valor_saque > 500:
            print('Operação negada! O limite para cada operação de saque é de R$500.')           
        else:
            print(f'Saque de R${valor_saque:.2f} realizado com sucesso!')
            saldo -= valor_saque
     
    elif option =='E':
        print(f'Saldo atual R${saldo:.2f}')

    elif option == 'F':
        print('Finalizando...')
        break       
            
        
                
    