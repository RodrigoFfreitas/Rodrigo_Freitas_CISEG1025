import re

with open("E:/DEV/Rodrigo_Freitas_CISEG1025/UC01481/ex_REGEX_txt/dados.txt", "r") as ficheiro:
    conteudo = ficheiro.read()

print("=== Conteudo do ficheiro ===")
print(conteudo)
print("\n")


regexTelemovel = r"\b\d{9}\b|\b\d{3}-\d{3}-\d{3}\b|\b\d{3} \d{3} \d{3}\b"
telemoveis = re.findall(regexTelemovel, conteudo)

print("=== Números de telemóvel encontrados ===")
for tel in telemoveis:
    print(tel)
print("\n")