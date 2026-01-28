p1opc=""
p2opc=""


p1opc=input("Player1 - Pedra, Papel ou Tesoura?  ")
p2opc=input("Player2 - Pedra, Papel ou Tesoura?  ")

match p1opc.lower():
    case "pedra":
        match p2opc.lower():
            case "pedra":
                print("Empate")
            case "papel":
                print("Vitória do Player 2")
            case "tesoura":
                print("Vitoria do Player 1")
            case _:
                print("Escolha do Player 2 Inválida.")
    case "papel":
        match p2opc.lower():
            case "pedra":
                print("Vitoria do Player 1")
            case "papel":
                print("Empate")
            case "tesoura":
                print("Vitoria do Player 2")
            case _:
                print("Escolha do Player 2 Inválida")
    case "tesoura":
        match p2opc.lower():
            case "pedra":
                print("Vitoria do Player 2")
            case "papel":
                print("Vitoria do Player 1")
            case "tesoura":
                print("Empate")
            case _:
                print("Escolha do Player 2 Inválida")
    case _:
        print("Escolha do Player 1 Inválida.")
