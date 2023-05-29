'''4. Faça um programa que leia dois números inteiros e que imprima todos os números inteiros existentes entre o menor e o maior número informados.'''

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 < numero2:
    for i in range(numero1, numero2 + 1):
        print(i)
else:
    for i in range(numero2, numero1 + 1):
        print(i)