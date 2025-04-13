conta_nomral = False
conta_universitaria = True

saldo = 1800
saque = 100
cheque_especial = 600


if conta_nomral:
    if saldo >= saque:
        print("Saque realizado")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado utilizando cheque especial!")
    else:
        print("não foi possivel realizar o saque. Saldo insuficiente")
elif conta_universitaria:
    if saldo >= saque:
        print("saque realizado")
    else:
        print("saldo insuficiente")