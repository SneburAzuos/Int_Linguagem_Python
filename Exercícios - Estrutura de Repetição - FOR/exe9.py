'''9. Faça um programa que leia a idade e peso de sete pessoas. Calcule e mostre:
	- a quantidade de pessoas com mais de 90 kg
	- a média das idades das sete pessoas
'''

soma_idades = 0
mais_de_90kg = 0

for i in range(1, 8):
    idade = int(input("Digite a idade da pessoa " + str(i) + ": "))
    peso = float(input("Digite o peso da pessoa " + str(i) + ": "))

    soma_idades += idade

    if peso > 90:
        mais_de_90kg += 1

media_idades = soma_idades / 7

print("Quantidade de pessoas com mais de 90 kg:", mais_de_90kg)
print("Média das idades das sete pessoas:", media_idades)