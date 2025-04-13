nome = input("Diga seu nome:")
idade = int(input("diga sua idade:"))
curso = input("Qual o curso que você está fazendo agora:")

# Meotodo FORMAT
print("Olá {}, acho muito interresante alguém com {} anos de idade fazendo este curso de {}. Parabén pela sua determinação!.".format(nome, idade, curso))

print("Olá {2}, acho muito interresante alguém com {0} anos de idade fazendo este curso de {1}. Parabén pela sua determinação!.".format(idade, curso, nome))

# Metodo F - STRING

print(f"Olá {nome}, acho muito interresante alguém com {idade} anos de idade fazendo este curso de {curso}. Parabén pela sua determinação!.") 