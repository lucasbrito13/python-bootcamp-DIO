print ("Operador E (and)")
# ambos precisam ser possitivos para o resultado ser possitivo
print (True and True)
print (True and False)
print (False and True)
print (False and False)


print("Operador OU (or)")
# Um dos argumentos precisam ser verdadeiros
print (True or True)
print (True or False)
print (False or True)
print (False or False)

print ("Operador de negação (not)")
# Basicamente o contrario
print("not e and")
print (not True and True)
print (not True and False)
print (not False and True)
print (not False and False)



print("exemplo")
saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

print(exp)


exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)