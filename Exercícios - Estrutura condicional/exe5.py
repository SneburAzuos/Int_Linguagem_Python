'''. Faça um programa que leia o sexo e a altura (H - em metros) de uma pessoa, 
calcule e apresente seu peso ideal utilizando as seguintes fórmulas: 

Peso ideal (homens) = (72,7 * H) – 58. 
Peso ideal (mulheres) = (62,1 * H) – 44,7'''

sexo = input("Qual é o seu sexo  digite M para masculino ou F para feminino)? ")
altura = float(input("Qual é a sua altura em metros? "))

if sexo.upper() == 'M':
    peso_ideal = (72.7 * altura) - 58
elif sexo.upper() == 'F':
    peso_ideal = (62.1 * altura) - 44.7

print("Seu peso ideal é:", peso_ideal)