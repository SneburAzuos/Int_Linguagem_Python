'''1. Faça um programa que receba dois números e mostre o maior e o menor. 
Emita uma mensagem, caso os dois sejam iguais.'''

num1 = int(input('Entre com o primeiro numero:'))
num2 = int(input('Entre com segundo numero:'))

if num1 > num2:
    print('O numero,', num1,'é o maior.')
    print('O numero,', num2,'é o menor.')
else:
    print('Os numeros são iguais!')   