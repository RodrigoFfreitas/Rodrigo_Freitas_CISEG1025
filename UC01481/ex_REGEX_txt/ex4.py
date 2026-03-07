import re

with open("E:/DEV/Rodrigo_Freitas_CISEG1025/UC01481/ex_REGEX_txt/dados.txt", "r") as ficheiro:
    conteudo = ficheiro.read()

print("=== Conteudo do ficheiro ===")
print(conteudo)
print("\n")

regexNome = r"Nome: ([\w\s]+),"
nomes = re.findall(regexNome, conteudo)

print("=== Nomes extraídos ===")
for nome in nomes:
    print(nome)
print("\n")