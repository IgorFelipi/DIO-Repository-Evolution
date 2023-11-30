menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> Digite a letra que deseja:  """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Digite a quantidade que vai depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito de: R$ {valor:.2f}\n"
        else:
            print("Falha na Operação! \nInsira um valor valido")
    
    elif opcao == "s":
        valorSaque = float(input("Digite o valor do saque: "))
        
        excedeu_saldo = valorSaque > saldo
        
        excedeu_limite = valorSaque > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha na Operação! Saldo indisponivel para saque")
        
        elif excedeu_limite:
            print("Falha na Operação! Excedeu o limite diário de saque") 
        
        elif excedeu_saques:
            print("Falha na Operação! Limite de saques diarios excedido!")
        
        elif valorSaque > 0:
            saldo -= valorSaque
            extrato += f"Saque de: R$ {valorSaque:.2f}\n"
            excedeu_saques += 1
        else:
            print("Falha na Operação! \nInsira um valor valido")
    
    elif opcao == "e":
        print("\n ===============EXTRATO============")
        print("\n Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo da conta: R$ {saldo:.2f}")
        print("======================================")

    elif opcao == "q":
        break
    
    else:
        print("Operação inválida! \nDigite uma letra correspondente")
