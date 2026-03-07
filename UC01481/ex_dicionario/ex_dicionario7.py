dicionario = {
    "a": 1,
    "b": 2,
    "c": 3
}

dicionarioInvertido = {}

for chave, valor in dicionario.items():
    dicionarioInvertido[valor] = chave

print(dicionarioInvertido)