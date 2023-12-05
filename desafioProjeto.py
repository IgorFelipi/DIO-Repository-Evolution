import textwrap


def menu(): 
    menu = """\n
    ================= MENU =============

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuario
    [q] \tSair

    => Informe a Operação:  """
    return input(textwrap.dedent(menu))


def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito \t: R$ {valor:.2f}\n"
        print("\n===Desposito realizado com sucesso!===")
    else:
        print("\n@@@Falha na Operação! Insira um valor valido. @@@")
    
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print("\n@@@Falha na Operação! Saldo indisponivel para saque. @@@")
        
    elif excedeu_limite:
        print("\n@@@Falha na Operação! Excedeu o limite diário de saque.@@@") 
        
    elif excedeu_saques:
        print("\n@@@Falha na Operação! Limite de saques diarios excedido! @@@")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque \t\t: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n===Saque realizado com sucesso!===")
    else:
        print("\n@@@Falha na Operação! \nInsira um valor valido. @@@")
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n ===============EXTRATO============")
    print("\n Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n Saldo da conta: R$ {saldo:.2f}")
    print("======================================")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def cadastrar_usuario(usuarios):
    cpf = int(input("Por favor informe o CPF(Somente numeros): "))
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n@@@ Já existe um usuario com este CPF! @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aa): ")
    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla do estado: )")

    usuarios.append({"nome": nome, "data de nascimento": data_nascimento, "cpf": cpf, "Endereço": endereco})
    
    print("=== Usuario cadastrado com Sucesso! ===")


def nova_conta(agencia, numero_conta, usuarios):
    cpf = int(input("Por favor informe o CPF(Somente numeros): "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso!===")
        return {"Agencia": agencia, "Numero da conta": numero_conta, "Usuario": usuario}
    
    print("\n@@@ USUARIO NÃO ENCONTRADO, CRIAÇÃO DE CONTA ENCERRADA!@@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t {conta["Agencia"]}
            C/C:     \t {conta["Numero da conta"]}
            Titular: \t {conta["Usuario"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    
    LIMITE_SAQUES = 3 
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    qtd_contas = 1
    
    while True:
    
        opcao = menu()
    
        if opcao == "d":
            valor = float(input("Digite a quantidade que vai depositar: "))
            saldo, extrato = deposito(saldo, valor, extrato)
    
        elif opcao == "s":
            valor = float(input("Digite o valor do saque: "))
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite= limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            cadastrar_usuario(usuarios)
        
        elif opcao == "nc":
            conta = (nova_conta(AGENCIA, qtd_contas, usuarios))
            if conta:
                contas.append(conta)
                qtd_contas += 1
        
        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "q":
            break
    
        else:
            print("@@@Operação inválida! \nDigite uma letra correspondente @@@")


main()