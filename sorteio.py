import random
numeros = []
while len(numeros) < 10:
    numero = random.randint(1, 100)
    if numero not in numeros:
        numeros.append(numero)
        print(sorted(numeros))