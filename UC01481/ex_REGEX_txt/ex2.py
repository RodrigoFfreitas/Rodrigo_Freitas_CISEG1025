import re

with open("E:/DEV/Rodrigo_Freitas_CISEG1025/UC01481/ex_REGEX_txt/dados.txt", "r") as ficheiro:
    conteudo = ficheiro.read()

regexEmail = r"[\w\.-]+@[\w\.-]+\.\w+"
emails = re.findall(regexEmail, conteudo)

print("=== Emails encontrados ===")
for email in emails:
    print(email)
print("\n")