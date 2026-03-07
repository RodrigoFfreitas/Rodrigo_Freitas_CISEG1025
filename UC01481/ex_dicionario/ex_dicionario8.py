dicionario1 = {
    "a": 1,
    "b": 2
}

dicionario2 = {
    "c": 3,
    "d": 4
}

dCombinado = {}

# Adiciona os pares de dicionario1
for chave, valor in dicionario1.items():
    dCombinado[chave] = valor

# Adiciona os pares de d2
for chave, valor in dicionario2.items():
    dCombinado[chave] = valor

print(dCombinado)