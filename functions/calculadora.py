def soma(A, B):
    resultado = A + B
    return resultado

def subtracao(A, B):
    resultado = A - B
    return resultado

def divisao(A, B):
    if(B == 0):
        return("Não é possível efetuar divisão por 0")
    resultado = A / B
    return resultado

def multiplicacao(A, B):
    resultado = A * B
    return resultado

def requisitaValores():
    A = int(input("Digite o valor A: "))
    B = int(input("Digite o valor B: "))
    return A, B

def principal():
    A, B = requisitaValores()
    print("Soma: ", soma(A, B))
    print("Subtração: ", subtracao(A, B))
    print("Divisão: ", divisao(A, B))
    print("Multiplicação: ", multiplicacao(A, B))

if __name__ == "__main__":
    principal()