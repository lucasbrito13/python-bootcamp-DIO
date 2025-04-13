def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, function):
    resultado = function(a, b)
    print(f"O Resultado é = {resultado} ")


exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)


usando_em_uma_variavel = somar

print(usando_em_uma_variavel(1, 24))