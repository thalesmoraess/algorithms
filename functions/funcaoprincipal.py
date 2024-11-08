def quadrado(valor):
    resultado = valor * 2
    return resultado

def soma(valor1, valor2):
    resultado = valor1 + valor2
    return resultado

def requisitaValores():
    valorA = int(input("Digite o valor A: "))
    valorB = int(input("Digite o valor B: "))
    return valorA, valorB

def principal():
    valorA, valorB = requisitaValores()
    valorC = quadrado(valorA)
    valorD = quadrado(valorB)
    valorE = soma (valorC, valorB)
    print(valorE)

if __name__ == "__main__":
    principal()