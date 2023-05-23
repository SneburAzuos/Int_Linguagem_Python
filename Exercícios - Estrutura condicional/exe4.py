'''4. Dados três valores X,Y,Z, verificar se eles podem ser os comprimentos dos
lados de um triângulo. Se eles não formarem um triângulo escrever uma mensagem. 
Considerar que o comprimento de cada lado de um triângulo é menor que a soma 
dos outros dois lados.'''

x = float(input("Digite o valor de X: "))
y = float(input("Digite o valor de Y: "))
z = float(input("Digite o valor de Z: "))

if x + y > z and x + z > y and y + z > x:
        print("É um triângulo!")
else:
        print("Não é um triângulo.")

