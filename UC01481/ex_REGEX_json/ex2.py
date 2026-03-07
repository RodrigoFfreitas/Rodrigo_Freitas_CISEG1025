import json
import re

with open("E:/DEV/Rodrigo_Freitas_CISEG1025/UC01481/ex_REGEX_json/dados.json", "r") as ficheiro:
    listaDados = json.load(ficheiro)

regexEmail = r"^[\w\.-]+@[\w\.-]+\.\w+$"
print("=== Validação de Emails ===")
for registo in listaDados:
    email = registo["email"]
    if re.match(regexEmail, email):
        print(f"Email válido: {email}")
    else:
        print(f"Email inválido: {email}")
print("\n")
