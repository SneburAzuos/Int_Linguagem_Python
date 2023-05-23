'''. Faça um programa que receba 3 notas de um aluno, 
calcule e mostre uma mensagem de acordo com sua média:

MÉDIA	        MENSAGEM
>= 0 e < 3 	    REPROVADO 
>= 3 e < 7 	    EXAME 
>= 7 e <= 10 	APROVADO'''

nota1 = float(input('Digie a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3)/3

if (media >= 0 and media < 3 ):
    print('Reprovado!')
elif (media >= 3 and media < 7 ):
    print('Exame!')
else:
    print('Aprovado!')
    
