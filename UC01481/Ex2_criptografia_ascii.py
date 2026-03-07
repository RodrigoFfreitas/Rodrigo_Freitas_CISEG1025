def calcular_chave(chave: str) -> int:
    if len(chave) == 0:
        print("Erro: a chave não pode ser vazia.")
        exit()

    soma = 0
    for c in chave:
        soma += ord(c)
    return soma


def criptografar(mensagem: str, chave: str) -> list:
    chave_numerica = calcular_chave(chave)
    codigos = []

    for c in mensagem:
        ascii_original = ord(c)

        # rotação no intervalo 32–126
        ascii_criptografado = 32 + ((ascii_original - 32 + chave_numerica) % 95)

        codigos.append(ascii_criptografado)

    return codigos


def descriptografar(codigos: list, chave: str) -> str:
    chave_numerica = calcular_chave(chave)
    mensagem = ""

    for codigo in codigos:
        # rotação inversa
        ascii_original = 32 + ((codigo - 32 - chave_numerica) % 95)
        mensagem += chr(ascii_original)

    return mensagem


def listar(codigos: list):
    print("Mensagem criptografada (códigos ASCII):")
    for codigo in codigos:
        print(codigo, end=" ")
    print()


mensagem = input("Introduz a mensagem: ")
chave = input("Introduz a chave: ")

codigos = criptografar(mensagem, chave)
listar(codigos)

mensagem_original = descriptografar(codigos, chave)
print("Mensagem descriptografada:", mensagem_original)