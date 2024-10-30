x = int(input("Digite um número inteiro: "))
y = int(input("Digite outro número inteiro: "))
z = int(input("Digite um terceiro número inteiro: "))

if y > x:
    if z > y:
        print(z, "É maior")
    else:
        print(y, "É maior")
else:
    if z > x:
        print(z, "É maior")
    else:
        print(x, "É maior")