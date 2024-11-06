def pertence_fi(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return "Pertence à sequência de Fibonacci" if b == num else "Não pertence à sequência de Fibonacci"

num = int(input("Digite um número: "))
print(pertence_fi(num))