'''2. Solicite ao usuário que digite uma frase. Em seguida, 
solicite ao mesmo que digite uma palavra. Imprima uma mensagem
informando a quantidade de vezes em que a palavra se encontra
na frase (considere que a palavra pode estar em maiúscula ou minúscula na frase).'''

frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra: ")

qtd_palavra = frase.lower().count(palavra.lower())

print(f"A palavra '{palavra}' aparece {qtd_palavra} vezes na frase.")