

valor = "123"

match valor:
    case int():
        print("Número inteiro")
    case float():
        print("Número decimal")
    case str() if valor.isdigit():   # a função isdigit analisa se todos os caracteres da string são numeros, se verdadeiro então a string é numérica, se falso então a string é textual
        print("String numérica")
    case str():
        print("String textual")
    case list():
        print("Lista")
    case _:
        print("Tipo desconhecido")
