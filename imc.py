def IMC():
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))

    imc = peso / (altura ** 2)

    print("Seu IMC é: %2.2f" % imc)