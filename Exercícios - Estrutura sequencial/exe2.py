# pylint: disable=missing-final-newline
#2.	Faça um programa que receba o ano de nascimento de uma pessoa" 
#o ano atual e imprima:
#a.	A idade da pessoa no ano atual
#b.	A idade que a pessoa terá em 2050

anoNascimento = int(input("Digite seu ano de nascimento? "))
anoAtual = int(input("Digite o ano atual? "))
idade =  anoAtual - anoNascimento
idade1 = 2050 - anoNascimento
print("Ano de nascimento é:", anoNascimento)
print("Ano atual é:", anoAtual)
print("Sua idade neste no ano é:", idade)
print("Sua idade em 2050 será:", idade1)