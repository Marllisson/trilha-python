##Programa gerencia atvidade da conta de banco
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


saldo = 0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        valor = float(input("Informe o valor para Depósito: "))
        
        if valor < 0:
            print("Valor inválido!")
        else:
            saldo += valor
            extrato += f"Deposito: RS {valor:.2f}\n"

    elif opcao == "s":
        print("Saque")

        valor = float(input("Informe o valor para saque: "))

        execeudeu_saldo = valor > saldo

        execeudeu_limite = valor > limite

        execedeu_numeros_saques = numero_saques >= LIMITE_SAQUE



        if execeudeu_saldo:
            print("Operação invalida, saldo insuficiente!")
        
        elif execeudeu_limite:
            print("Operação invalida, valor de saque maior que limite!") 
        
        elif execedeu_numeros_saques:
            print("Operação invalida, você excedeu o numero de saques.")
         
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: RS {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Valor invalido!")
            

    
    elif opcao == "e":
        print("\n===========EXTRATO==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==============================")
    
    elif opcao == "q":
        break

    else:
        print("Operação invalida por favor selecione novamente a operação desejada")