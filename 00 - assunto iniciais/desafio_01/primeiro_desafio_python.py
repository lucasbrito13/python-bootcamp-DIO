menu = '''
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu.center(20,"="))

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Deposito de {valor} realizado com sucesso!")
        
        else:
            print("Operação falhou!! O Valor informado é invalido.")

    elif opcao == "2":
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("""
                  Operação Falhou!! Você não possui saldo suficiente.
                  Verifique o seu extrato!
                  """)
        elif excedeu_limite:
            print(f"Operação falhou! Você excedeu o limite de {float(limite)} por saque.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numero_saques += 1
        
        else:
            print("Operação falhou! O valor informado é invalido.")