""". Faça um programa que, tendo como dados de entrada a altura (H - em metros) de uma mulher, 
calcule e apresente seu peso ideal utilizando a seguinte fórmula:
Peso ideal (P) = (62,1 * H) – 44,7
"""

h = float(input("Digite a altura em metros: "))
peso_ideal = 62.1 * h - 44.7
peso_ideal_str = str(peso_ideal).split(".")[0] # remove a parte decimal sem arredondar
print("O peso ideal é", peso_ideal_str, "kg")