saldo = 200
saque = 50

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar saque!")