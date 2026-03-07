import json
import re

with open("E:/DEV/Rodrigo_Freitas_CISEG1025/UC01481/ex_REGEX_json/dados.json", "r") as ficheiro:
    listaDados = json.load(ficheiro)
    
regexNIF = r"^[123568]\d{8}$"
print("=== Validação de NIFs ===")
for registo in listaDados:
    nif = registo["nif"]
    if re.match(regexNIF, nif):
        print(f"NIF válido: {nif}")
    else:
        print(f"NIF inválido: {nif}")
print("\n")