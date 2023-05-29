'''1. Solicite ao usuário que digite uma frase. Imprima:
	- o tamanho (em caracteres) da frase
	- a frase toda em maiúscula
	- a frase toda em minúscula
	- a frase na vertical(letra por letra)
	- solicite ao usuário que informe uma posição inicial e final na frase, e imprima a parte da frase que se encontra dentro das posições informadas pelo usuário
	- a frase em ordem inversa
	- solicite ao usuário que informe duas palavras. Substitua, na frase informada, a primeira palavra informada pelo usuário, pela segunda palavra informada. Armazene a nova frase em uma nova variável, e imprima o conteúdo da nova variável.
'''

frase = input("Digite uma frase: ")

print(f"Tamanho da frase: {len(frase)}")
print(f"Frase em maiúscula: {frase.upper()}")
print(f"Frase em minúscula: {frase.lower()}")

print("Frase na vertical:")
for letra in frase:
    print(letra)

inicio = int(input("Digite a posição inicial: "))
fim = int(input("Digite a posição final: "))
print(f"Parte da frase entre as posições {inicio} e {fim}: {frase[inicio:fim]}")

print(f"Frase em ordem inversa: {frase[::-1]}")

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")
nova_frase = frase.replace(palavra1, palavra2)
print(f"Nova frase: {nova_frase}")