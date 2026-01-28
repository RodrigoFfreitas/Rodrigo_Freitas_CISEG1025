

nota=''

print("|Exelente/Bom/Suficiente/Insuficiente|")
nota = input("Insira a Classificação: ")

match nota.lower():
    case "exelente":
        print("De 90 para cima")
    case "bom":
        print("70 - 89")
    case "suficiente":
        print("50 - 69")
    case "insuficiente":
        print("Abaixo de 50")
    case _:
        print("A Classificação Inserida é inválida, deve escolher uma das seguintes Classificações: |Exelente/Bom/Suficiente/Insuficiente|")