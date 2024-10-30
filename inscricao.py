nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Menor de idade.")
    print("Não é permitida sua inscrição.")
else:
    print("Maior de idade.")
    sexo=str(input("Digite (F) - Feminino, (M) - Masculino: ").upper()) # upper() - comando que converte a letra em maiúscula

    if sexo == "M":
        print("Sexo Masculino.")
        print("Número CAM: ")
    elif sexo == "F":
        print("Sexo Feminino.") # para o sexo feminino não pede documento
    else:
        print("Sexo inválido.")