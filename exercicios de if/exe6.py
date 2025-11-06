compra=0
desconto=0

compra=float(input("Insira o valor da sua compra: "))


if compra <= 200.00:
    print(f"Compra: {compra}€")
    desconto = (compra * 0.10)
    print(f"Desconto: {desconto}€")
    compra = compra - desconto 
    print(f"Total a Pagar: {compra}€")
elif compra > 200.00 and compra <= 500.00:
    print(f"Compra: {compra}€")
    desconto = (compra * 0.15)
    print(f"Desconto: {desconto}€")
    compra = compra - desconto 
    print(f"Total a Pagar: {compra}€")
else:
    print(f"Compra: {compra}€")
    desconto = (compra * 0.20)
    print(f"Desconto: {desconto}€")
    compra = compra - desconto 
    print(f"Total a Pagar: {compra}€")