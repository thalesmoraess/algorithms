# transferindo os valores de uma lista/tupla para variáveis individuais.

lista = [10, 20, 30, 40, 50]
for idx, item in enumerate(lista):
    if idx == 0:
        a = item
    else:
        b = item
print("a=", a, "b=", b)