'''7. Uma empresa decide dar aumento de 30% aos funcionários com salários inferiores a R$1000,00. 
Faça um programa que receba o salário do funcionário e mostre o valor do salário reajustado 
ou uma mensagem, caso o funcionário não tenha direito ao aumento.'''

salario = float(input("Digite o salário do funcionário: "))

if salario < 1000:
    salario_reajustado = salario * 1.3
    print("Salário reajustado:", salario_reajustado)
else:
    print("O funcionário não tem direito ao aumento.")