'''10. Faça um programa que leia um número e que imprima na tela se o número é primo ou não.'''

numero = int(input("Digite um número inteiro: "))

if numero > 1:
    for i in range(2, numero):
        if (numero % i) == 0:
            print(numero, "não é primo")
            break
    else:
        print(numero, "é primo")
else:
    print(numero, "não é primo")