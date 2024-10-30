temp = int(input("Qual a temperatura?: "))

if temp < 5:
    print("Congelando")
elif 0 <= temp <= 10:
    print("Frio")
elif 20 <= temp <= 25:
    print("Normal")
elif 26 <= temp <= 35:
    print("Muito quente!")