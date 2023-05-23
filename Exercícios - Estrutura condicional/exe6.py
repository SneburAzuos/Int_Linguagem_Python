#6. Construa um programa para determinar se o indivíduo está com um peso 
#favorável. Essa situação é determinada através do IMC (Índice de Massa 
#Corpórea), que é definida como sendo a relação entre o peso (PESO – em 
#kg) e o quadrado da Altura (ALTURA – em m) do indivíduo. Ou seja,
#IMC= PESO/ALTURA2 e, a situação do peso é determinada pela tabela abaixo:
'''Condição	Situação
IMC abaixo de 20	Abaixo do peso
IMC de 20 até 25	Peso Normal
IMC de 25 até 30	Sobre Peso
IMC de 30 até 40	Obeso
IMC de 40 e acima	Obeso Mórbido'''

peso = float(input('Informe seu peso em Kg:'))
altura = float(input('Informe a altura:'))

IMC = peso / (altura ** 2)

if (IMC < 20):
    print('Abaixo do peso.')
elif (IMC >= 20 and IMC < 25):
    print('Peso normal.')
elif (IMC >= 25 and IMC < 30):
    print('Sobre peso.') 
elif (IMC >= 30 and IMC < 40):
    print('Obeso')
else:
    print('Obesidade morbida')               