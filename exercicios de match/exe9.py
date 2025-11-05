
metodo = "POST"
conteudo = ""


match metodo:
    case "GET":
        print("Requisição GET recebida")
    case "POST":
        if conteudo == "":
            print("Requisição POST sem dados")
        else:
            print("Requisição POST com dados válidos")
    case _:
        print("Método não suportado")
