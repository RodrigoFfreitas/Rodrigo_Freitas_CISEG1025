saldo=0
cheque=0

saldo=int(input("Saldo: "))
cheque=int(input("Cheque: "))


if saldo >= cheque:
    saldo = saldo - cheque
    print(f"Cheque descontado, saldo: {saldo}")
else:
    print(f"O cheque não pode ser descontado, saldo insuficiente.")
    
