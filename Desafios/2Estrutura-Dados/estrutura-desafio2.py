import textwrap
##Programa gerencia atvidade da conta de banco


def menu():
    menu = """\n
    ============= MENU ==========
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\Sair

    ==>"""
    return input(textwrap.dedent(menu))

# Função depositar que recebe paramentro por posicional only. Lembrete: Deve ser inserido a barra no final.
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f} \n"
        print("\n=== Deposito realizado com sucecsso! ===")
    else:
        print("\n@@@ Operação falhou! Valor informado é inválido. @@@")

    return saldo, extrato

# Função Saque que recebe parametros por keyword. Lembrete: Deve apresentar * no inicio
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\@@@ Operação falhou! Você não possui saldo suficiente. @@@") 
    
    elif excedeu_limite:
        print("\@@@ Operação falhou! Saque excedeu o limite. @@@") 

    elif excedeu_saque:
        print("\@@@ Operação falhou! Número máximo de saques excedido. @@@") 
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n === Saque realizado com sucesso! ===")
    else:
        print("\n @@@ Operação falhou. O valor informado é invalido. @@@")


    return saldo, extrato

# Função que apresenta o extrato
def exibir_extrato(saldo,/,*,extrato):
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("================================")

# Função que cria novo usuário
def criar_usuario(usuarios):
    cp = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n@@@ Já existe usuário com este CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço(logradour, nro - bairo - cidade/sigla estado): ")

    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf":cpf, "endereco":endereco})

    print("=== Usuário cadastrado com sucesso! ===")

# Funçaõ que filtra usuario
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuarios in usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# Funcção para criação de conta
def criar_conta(agencia, numero_conta, usuraios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuraios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n@@@ Usuário não encontrado, fluxo de crtiação de conta encerrado! @@@")

# Função que lista as contas
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario'] ['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

    

def main():
    
    
    LIMITE_SAQUES = 3 
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = " "
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        
        opcao = menu()
        #Antigo Progrma de controle de conta
        # LIMITE_SAQUE = 3 
        # saldo = 0
        # limite = 500
        # extrato = " "
        # numero_saques = 0
         
        #menu = """
        #[d] Depositar
        #[s] Sacar
        #[e] Extrato
        #[q] Sair
        #=> """
        #opcao = input(menu)
        #antigo bloco para executar deposito
        #if opcao == "d":
        #    print("Deposito")
        #    valor = float(input("Informe o valor para Depósito: "))
        #    
        #    if valor < 0:
        #        print("Valor inválido!")
        #    else:
        #        saldo += valor
        #        extrato += f"Deposito: RS {valor:.2f}\n"
        #
        #Antigo Bloco de extrato
        # elif opcao == "e":
        #     print("\n===========EXTRATO==========")
        #     print("Não foram realizadas movimentações." if not extrato else extrato)
        #     print(f"\nSaldo: R$ {saldo:.2f}")
        #     print("==============================")
        # 

        # Novo bloco de execução do deposito
        if opcao == "d":
            valor = float(input("Informe o valor de deposito: "))
            #Função Depositar utilizar passagem posicional de parâmetros
            saldo, extrato = depositar(saldo, valor, extrato) 

            #Antiga função de Saque 
            # """elif opcao == "s":
            #     print("Saque")
            
            #     valor = float(input("Informe o valor para saque: "))
            
            #     execeudeu_saldo = valor > saldo
            
            #     execeudeu_limite = valor > limite
            
            #     execedeu_numeros_saques = numero_saques >= LIMITE_SAQUE
            
            #     if execeudeu_saldo:
            #         print("Operação invalida, saldo insuficiente!")
                
            #     elif execeudeu_limite:
            #         print("Operação invalida, valor de saque maior que limite!") 
                
            #     elif execedeu_numeros_saques:
            #         print("Operação invalida, você excedeu o numero de saques.")
                
            #     elif valor > 0:
            #         saldo -= valor
            #         extrato += f"Saque: RS {valor:.2f}\n"
            #         numero_saques += 1

            #     else:
            #         print("Valor invalido!")
            # """        
        # Nova Chamanda para função de Saque
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))        
            #Chamada funcção de sacar que utilizar passagem de parametros com palavras chaves,keywords.
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )
        # Novo Bloco de Extrato
        elif opcao == "e":
            #Função utilizar passagem de parametros tanto posicional quanto palavra chave
            exibir_extrato(saldo, extrato = extrato)        
        # Comando que cria usuarios
        elif opcao == "nu":
            #Função que cria ususário
            criar_usuario(usuarios)
        # Bloco responsável por criar contas
        elif opcao == "nc":
            # numero_cta = len(contas) + 1
            # Funcao que cria contas
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1
        # Bloco responsável por listar todas as contas criasdas
        elif opcao == "lc":
            listar_contas(contas)
        # Bloco Responsável por sair do programa
        elif opcao == "q":
            break
        # Condição responsável por verficar se a opção escolhida não faz parte da listada no menu
        else:
            print("Operação invalida por favor selecione novamente a operação desejada")



main()