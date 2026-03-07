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


regexNIF = r"^[123568]\d{8}$"
print("=== Validação de NIFs ===")
for registo in listaDados:
    nif = registo["nif"]
    if re.match(regexNIF, nif):
        print(f"NIF válido: {nif}")
    else:
        print(f"NIF inválido: {nif}")
print("\n")


regexTelemovel = r"^\d{9}$"

listaValidos = []

for registo in listaDados:
    emailValido = re.match(regexEmail, registo["email"])
    nifValido = re.match(regexNIF, registo["nif"])
    
    telemovelNumeros = re.sub(r"\D", "", registo["telemovel"])
    telemovelValido = re.match(regexTelemovel, telemovelNumeros)
    
    if emailValido and nifValido and telemovelValido:
        listaValidos.append(registo)

with open("E:/DEV/Rodrigo_Freitas_CISEG1025/UC01481/ex_REGEX_json/dados_validos.json", "w") as ficheiroValidos:
    json.dump(listaValidos, ficheiroValidos, indent=4)

print("Registos válidos guardados em 'dados_validos.json'.\n")