"""3.	Faça um programa que solicite ao usuário que informe os coeficientes a, 
#b e c de uma equação de segundo grau, e que imprima as raízes desta 
#equação (considere que os valores informados sempre retornarão raízes reais para a equação)."""


import math

a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

delta = b**2 - 4*a*c

if delta >= 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("As raízes da equação são:", x1, "e", x2)
else:
    print("A equação não possui raízes reais.")