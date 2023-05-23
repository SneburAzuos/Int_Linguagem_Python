'''2. Faça um programa que receba as duas notas de um aluno, 
calcule sua média, e que imprima a sua situação: 
>= 7 -> Aprovado
< 7 -> Reprovado'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media =  (nota1 + nota2)/2

if (media >=7):
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')