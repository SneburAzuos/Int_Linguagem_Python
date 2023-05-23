"""6.Todo restaurante, embora por lei não possa obrigar o cliente a pagar, 
cobra 10% para o garçom. 
Faça um programa que leia o valor gasto pelo cliente 
e informe o valor a ser pago de gorjeta."""

valor = float(input('Digite o valor gasto pelo cliente: R$ '))
gorjeta = valor * 0.1
print('O valor da gorjeta é de R$ {:.2f}'.format(gorjeta))
