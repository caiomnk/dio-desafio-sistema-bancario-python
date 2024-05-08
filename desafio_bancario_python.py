menu = """
=============== BANCO BANQUITO ==============
Olá cliente!
=> Selecione a operação desejada:

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair
=============================================
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "0":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Falha de Operação! O valor informado e inválido.")

    elif opcao == "1":
        valor = float(input("Infome o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha de Operação! Sem saldo suficiente em conta.")

        elif excedeu_limite:
            print("Falha de Operação! Valor de saque excede limite atual da conta.")

        elif excedeu_saques:
            print("Falha de Operação! Limite de 3 saques diário excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Falha na Operação! O valor informado e inválido.")

    elif opcao == "2":
        print("\n========== EXTRATO ===========")
        print("Sem movimentações recentes na conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================")


    elif opcao == "3":
        break

    else:
        print("Opção inválida, favor escolher uma das opções válidas no menu inicial.")




