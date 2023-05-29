'''8. Faça um programa que leia o sexo e o peso de 10 pessoas, 
e mostre quantas pessoas do sexo masculino possuem peso entre 60 e 80 kg, 
bem como a quantidade de mulheres que possuem peso entre 50 e 70 kg.'''

homens = 0
mulheres = 0

for i in range(1, 11):
    sexo = input("Digite o sexo da pessoa " + str(i) + " (M/F): ")
    peso = float(input("Digite o peso da pessoa " + str(i) + ": "))

    if sexo == "M" and peso >= 60 and peso <= 80:
        homens += 1

    if sexo == "F" and peso >= 50 and peso <= 70:
        mulheres += 1

print("Quantidade de homens com peso entre 60 e 80 kg:", homens)
print("Quantidade de mulheres com peso entre 50 e 70 kg:", mulheres)