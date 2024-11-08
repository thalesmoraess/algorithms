def quadrado(valor):
    resultado = valor * 2
    return resultado

def soma(valor1, valor2):
    resultado = valor1 + valor2
    return resultado

valorA = int(input("Digite o valor A: "))
valorB = int(input("Digite o valor B: "))
valorC = quadrado(valorA)
valorD = quadrado(valorB)
valorE = soma(valorC, valorD)
print(valorE)