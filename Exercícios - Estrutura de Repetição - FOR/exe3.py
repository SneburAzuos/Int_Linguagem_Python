'''3. Leia um número e imprima a tabuada de multiplicar deste número. Por exemplo, para o número 5:'''

numero = int(input("Digite um número para a tabuada: "))
for i in range(0, 11):
    print(numero, "x", i, "=", numero * i)