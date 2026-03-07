notas = {
    "João": [10, 13.5, 12.2],
    "Maria": [10, 15, 11],
    "Ana": [18.2, 19.5, 17.2]
}

for aluno, listaNotas in notas.items():
    somaNotas = sum(listaNotas)
    quantidadeNotas = len(listaNotas)
    media = somaNotas / quantidadeNotas
    print(aluno + ":", media)