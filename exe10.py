"""Faça um programa que leia duas variáveis e troque o conteúdo dessas duas variáveis. 
Em seguida, imprima o valor dessas variáveis invertido. Exemplo: A = 7, B = 9. Saída: A = 9, B = 7"""

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

A, B = B, A

print("A =", A, "B =", B)