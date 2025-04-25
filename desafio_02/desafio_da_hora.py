from datetime import datetime, date

menu = '''
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
=> '''

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_TRANSACOES = 10
transacoes_do_dia = 0
data_hoje = date.today()

while True:
    
    if date.today() != data_hoje:
        data_hoje = date.today()
        transacoes_do_dia = 0
        numero_saques = 0

    
    if date.today().weekday() in [5, 6]: 
        print("\nTransações não são permitidas nos finais de semana.")
        opcao = input("Digite [0] para sair ou qualquer outra tecla para continuar: ")
        if opcao == "0":
            print("Obrigado por usar o sistema bancário. Até logo!")
            break
        else:
            continue

    opcao = input(menu)

    if opcao == "1":  
        if transacoes_do_dia >= LIMITE_TRANSACOES:
            print("Você excedeu o número de transações permitidas para hoje.")
            continue

        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato.append(f"{hora} - Depósito: R$ {valor:.2f}")
            transacoes_do_dia += 1
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":  
        if transacoes_do_dia >= LIMITE_TRANSACOES:
            print("Você excedeu o número de transações permitidas para hoje.")
            continue

        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não possui saldo suficiente.")
        elif excedeu_limite:
            print(f"Operação falhou! O limite por saque é de R$ {limite:.2f}.")
        elif excedeu_saque:
            print(f"Você excedeu o limite de {LIMITE_SAQUES} saques por dia.")
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            transacoes_do_dia += 1
            hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato.append(f"{hora} - Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":  
        print("\n========== EXTRATO ===========")
        if not extrato:
            print("Ainda não há movimentações.")
        else:
            for transacao in extrato:
                print(transacao)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==============================\n")

    elif opcao == "0": 
        print("Obrigado por usar o sistema bancário. Até logo!")
        break

    else:
        print("Operação inválida. Por favor, selecione uma opção válida.")
