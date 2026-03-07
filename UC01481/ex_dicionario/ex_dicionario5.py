palavra = input("Introduz uma palavra: ")

contagemLetras = {}

for letra in palavra:
    if letra in contagemLetras:
        contagemLetras[letra] += 1
    else:
        contagemLetras[letra] = 1

print(contagemLetras)