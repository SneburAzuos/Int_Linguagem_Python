"""5.	Receba um número positivo, calcule e mostre:
a.	O número digitado ao quadrado
b.	O número digitado ao cubo
"""

numero = float(input('Digite um numero positivo: '))
numeroQuadrado = numero ** 2
numeroCubo = numero ** 3
raizQuadrada = numero **(1/2)
raizCubica = numero **(1/3)
print('O numero digitado a o quadrado é:', numeroQuadrado)
print('O numero digitado a o cubo é:', numeroCubo)
print('A raiz quadrada do numero é:',raizQuadrada)
print('A raiz cubica do numero é:',raizCubica)