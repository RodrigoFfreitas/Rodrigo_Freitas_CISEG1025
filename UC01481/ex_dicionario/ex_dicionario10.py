frase = input("Introduz uma frase: ")

contagemPalavras = {}

palavras = frase.split()

for palavra in palavras:
    if palavra in contagemPalavras:
        contagemPalavras[palavra] += 1
    else:
        contagemPalavras[palavra] = 1

print(contagemPalavras)