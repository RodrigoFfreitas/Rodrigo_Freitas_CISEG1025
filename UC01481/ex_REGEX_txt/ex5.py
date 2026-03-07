import re


with open("E:/DEV/Rodrigo_Freitas_CISEG1025/UC01481/ex_REGEX_txt/dados.txt", "r") as ficheiro:
    conteudo = ficheiro.read()

print("=== Conteúdo do ficheiro ===")
print(conteudo)
print("\n")


regexEmail = r"[\w\.-]+@[\w\.-]+\.\w+"
emails = re.findall(regexEmail, conteudo)

print("=== Emails encontrados ===")
for email in emails:
    print(email)
print("\n")


regexTelemovel = r"\b\d{9}\b|\b\d{3}-\d{3}-\d{3}\b|\b\d{3} \d{3} \d{3}\b"
telemoveis = re.findall(regexTelemovel, conteudo)

print("=== Números de telemóvel encontrados ===")
for tel in telemoveis:
    print(tel)
print("\n")


regexNome = r"Nome: ([\w\s]+),"
nomes = re.findall(regexNome, conteudo)

print("=== Nomes extraídos ===")
for nome in nomes:
    print(nome)
print("\n")

with open("E:/DEV/Rodrigo_Freitas_CISEG1025/UC01481/ex_REGEX_txt/extraidos.txt", "w") as ficheiroNovo:
    for i in range(len(nomes)):
        ficheiroNovo.write(f"{nomes[i]} | {emails[i]} | {telemoveis[i]}\n")

print("Ficheiro 'extraidos.txt' criado com sucesso.\n")