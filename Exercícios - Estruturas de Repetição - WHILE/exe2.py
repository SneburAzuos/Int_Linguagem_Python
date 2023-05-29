'''2. Leia a idade de um número indeterminado de pessoas. Imprima:
- Quantas pessoas possuem idade acima de 50 anos
- A média de idade das pessoas
- O percentual de pessoas com idade abaixo de 40 anos
A leitura será encerrada quando o usuário informar uma idade negativa.
'''

idades = []
idade = 0

while idade >= 0:
    idade = int(input("Digite a idade da pessoa (ou um número negativo para sair): "))

    if idade >= 0:
        idades.append(idade)

qtd_acima_50 = len([i for i in idades if i > 50])
media_idades = sum(idades) / len(idades)
percentual_abaixo_40 = len([i for i in idades if i < 40]) / len(idades) * 100

print(f"Quantidade de pessoas com idade acima de 50 anos: {qtd_acima_50}")
print(f"Média de idade das pessoas: {media_idades:.2f}")
print(f"Percentual de pessoas com idade abaixo de 40 anos: {percentual_abaixo_40:.2f}%")