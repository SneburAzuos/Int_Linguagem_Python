'''Faça um programa que receba a idade de um nadador e mostre a sua categoria
IDADE	        CATEGORIA
até 7 anos	    INFANTIL
8 a 10 anos	    JUVENIL
11 a 15 anos	ADOLESCENTE
16 a 30 anos	ADULTO
acima de 30 anos	SENIOR

'''
idade = int(input('Digite sua idade:'))

if(idade <= 7):
    print('Categoria infantil.')
elif(idade >= 8 and idade <=10):
    print('Categoria juvenil.')
elif(idade >= 11 and idade <=15):
    print(' Categoria Adolescente.')
elif(idade >= 16 and idade <=30):
    print(' Categoria Adulto.')    
else:
    print('Categoria senior.')
