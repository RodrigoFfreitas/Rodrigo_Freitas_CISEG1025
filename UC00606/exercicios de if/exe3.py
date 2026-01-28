
num1=0
num2=0


num1=int(input("Insira o primeiro numero: "))
num2=int(input("Insira o segundo numero: "))


if num1 < num2:
    print(f"Crescente: {num1}, {num2}\nDecrescente: {num2}, {num1}")
else:
    print(f"Crescente: {num2}, {num1}\nDecrescente: {num1}, {num2}")