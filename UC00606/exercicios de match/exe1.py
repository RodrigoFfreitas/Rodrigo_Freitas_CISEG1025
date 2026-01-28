
opc=""

opc = input('Insira o dia da Semana: ')


match opc.lower():               # O variavel.lower() serve para transformar o input do user em lowercase para evitar problemas de maiusculas.
    case "segunda":
        print("Dia útil")
    case "terca":
        print("Dia útil")
    case "quarta":
        print("Dia útil")
    case "quinta":
        print("Dia útil")
    case "sexta":
        print("Dia útil")
    case "sabado":
        print("fim de semana")
    case "domingo":
        print("fim de semana")    
    case _:
        print("Insira apenas a primeira palavra do dia da semana, e sem caracteres expeciais!")
        
