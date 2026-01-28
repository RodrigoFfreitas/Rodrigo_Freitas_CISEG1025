categoria=""
preco=0.0

categoria=input("Insira a Categoria do Produto: ")
preco=float(input("Insira o Preço desse Produto: "))


match categoria.lower():
    case "alimento":
        print("Produto Alimentar!")
    case "eletronico" if preco <= 1000.0:
        print("Produto Comum")
    case "eletronico":
        print("Produto de Luxo")
    case _:
        print("Categoria dsconhecida")
        
        