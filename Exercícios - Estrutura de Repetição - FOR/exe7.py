'''7. Faça um programa que solicite ao usuário que informe o peso, em kg, de 10 pessoas, e em seguida, exiba a média desses pesos.'''

soma = 0

for i in range(1, 11):
    peso = float(input("Digite o peso da pessoa " + str(i) + ": "))
    soma += peso

media = soma / 10

print("A média dos pesos é", media)