mensagem = input("Escreva uma mensagem: ")

match mensagem.lower():
    case "bom dia" | "ola": 
        print("Saudação")
    case msg if msg.endswith("?"):                          # se a mensagem acabar com ?
        print("Pergunta")
    case msg if "tchau" in msg or "adeus" in msg:           # se a dentro da mensagem contiver tchau ou adeus
        print("Despedida")
    case _:
        print("Mensagem genérica")