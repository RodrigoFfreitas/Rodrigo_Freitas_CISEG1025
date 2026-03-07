nomes = [
    "Pedro Pereira",
    "Ana Beatriz",
    "Ana Clara",
    "Carlos Silva",
    "Beatriz Souza",
    "Ana Paula",
    "Pedro Andrade"
]


def ChaveOrdenar(nomeCompleto):
    partes = nomeCompleto.split()  # [primeironome apelido]
    primeiroNome = partes[0]
    apelido = partes[1]
    return (primeiroNome, apelido)  # tuple: primeiro ordena pelo primeiro nome, depois pelo apelido


nomes.sort(key=ChaveOrdenar)


for nome in nomes:
    print(nome)