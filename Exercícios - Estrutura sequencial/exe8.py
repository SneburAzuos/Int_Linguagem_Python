"""Faça um programa que, tendo como dados de entrada a altura (H - em metros) de um homem, 
calcule e apresente seu peso ideal utilizando a seguinte fórmula: 
Peso ideal (P) = (72,7 * H) – 58. 
"""

h = float(input("Digite a altura em metros: "))
peso_ideal = 72.7 * h - 58
peso_ideal_str = str(peso_ideal).split(".")[0] # remove a parte decimal sem arredondar
print("O peso ideal é", peso_ideal_str, "kg")