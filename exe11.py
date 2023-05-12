"""Considerando uma eleição de apenas dois candidatos, faça um programa que leia o número total de eleitores, 
o número de votos do primeiro candidato e o número de votos do segundo candidato. 
Em seguida, o programa deverá apresentar o percentual de votos de cada um dos candidatos 
e o percentual de votos nulos."""

eleitores = int(input("Digite o número total de eleitores: "))
votos_cand_1 = int(input("Digite o número de votos do candidato 1: "))
votos_cand_2 = int(input("Digite o número de votos do candidato 2: "))

total_votos = eleitores if eleitores > 0 else 1

porc_cand_1 = votos_cand_1 * 100 / total_votos
porc_cand_2 = votos_cand_2 * 100 / total_votos
porc_nulos = (total_votos - votos_cand_1 - votos_cand_2) * 100 / total_votos

print(f"Percentual de votos do candidato 1: {porc_cand_1:.2f}%")
print(f"Percentual de votos do candidato 2: {porc_cand_2:.2f}%")
print(f"Percentual de votos nulos: {porc_nulos:.2f}%")