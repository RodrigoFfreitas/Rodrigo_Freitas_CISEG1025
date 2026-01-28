
tipo=""
valor=0

print("Compra o Venda?")
tipo=input("Insira o tipo: ")

valor=float(input("Insira o valor: "))

match tipo.lower():
    case "compra":
        print(f"Compra de {valor}€")
    case "venda":
        print(f"Venda de {valor}€")
    case _:
        print("Tipo de transação inválida!")