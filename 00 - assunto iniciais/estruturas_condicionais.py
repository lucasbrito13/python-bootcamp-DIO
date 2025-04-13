MAIOR_IDADE = 18
IDADE_EXEDIDA = 16


idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode proseguir para tirar CNH!")

if idade < MAIOR_IDADE:
    print("Menor de idade, ainda não pode tirar CNH.")

if idade >= MAIOR_IDADE:
    print("Você já possui idade para tirar CNH. Prossiga!")
else:
    print("Você ainda não possui idade para tirar CNH.")

if idade >= MAIOR_IDADE:
    print("Você possui idade valida para tirar CNH, prossiga com os passos a seguir!")
elif idade == IDADE_EXEDIDA:
    print("Infelizmente você ainda é menor de idade, porém já pode fazer as aulas teóricas.")
else:
    print("Você ainda é menor de idade, ou não completou 18 anos para tirar CNH.")
