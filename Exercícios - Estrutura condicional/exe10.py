'''10. Faça um programa que leia um número inteiro entre 1 e 7 e escreva o dia da semana correspondente. 
Caso o usuário digite um número fora desse intervalo, 
deverá aparecer uma mensagem informando que não existe dia da semana com esse número.'''

numero = int(input("Digite um número inteiro entre 1 e 7: "))

if numero == 1:
    dia_semana = "Domingo"
elif numero == 2:
    dia_semana = "Segunda-feira"
elif numero == 3:
    dia_semana = "Terça-feira"
elif numero == 4:
    dia_semana = "Quarta-feira"
elif numero == 5:
    dia_semana = "Quinta-feira"
elif numero == 6:
    dia_semana = "Sexta-feira"
elif numero == 7:
    dia_semana = "Sábado"
else:
    dia_semana = "Não existe dia da semana com esse número"

print(f"O dia da semana correspondente ao número {numero} é: {dia_semana}")