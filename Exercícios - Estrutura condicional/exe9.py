'''9. Faça um programa que leia a idade de uma pessoa e informe a sua classe eleitoral: 
- não eleitor (abaixo de 16 anos); 
- eleitor obrigatório (entre a faixa de 18 e menor de 65 anos); 
- eleitor facultativo (de 16 até 18 anos e maior de 65 anos, inclusive)
'''

idade = int(input("Digite sua idade: "))

if(idade < 16):
    print('Não Eleitor.')
elif(16 <= idade <= 18 or idade >= 65):
    print('Eleitor Facultativo.')
else:
    print('Eleitor obrigatório.')

    