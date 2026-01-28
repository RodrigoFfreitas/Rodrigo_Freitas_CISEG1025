num1=0
num2=0
num3=0
maior=0
menor=0
meio=0

num1=int(input("Insira o primeiro numero: "))
num2=int(input("Insira o segundo numero: "))
num3=int(input("Insira o terceiro numero: "))


if num1 > num2 and num1 > num3:         # caso o numero 1 for o maior, a var maior = numero1
    maior = num1
    if num2 > num3:                     # sabendo que o num1 é o maior, se o num2 for maior que num3 o do meio é o num2 e o menor é o num3
        meio = num2
        menor = num3
    else:                               # caso contrario o num3 é o do meio e o num2 o menor
        meio = num3
        menor = num2
elif num2 > num1 and num2 > num3:       # caso o numero 2 for o maior, a var maior = numero2
    maior = num2
    if num1 > num3:                     # sabendo que o num2 é o maior, se o num1 for maior que num3 o do meio é o num1 e o menor é o num3
        meio = num1
        menor = num3
    else:                               # caso contrario o num3 é o do meio e o num2 o menor
        meio = num3
        menor = num1
elif num3 > num1 and num3 > num2:       # caso o numero 3 for o maior, a var maior = numero3
    maior = num3
    if num1 > num2:                     # sabendo que o num3 é o maior, se o num1 for maior que num2 o do meio é o num1 e o menor é o num2
        meio = num1
        menor = num2
    else:                               # caso contrario o num2 é o do meio e o num1 o menor
        meio = num2
        menor = num1 
    

# print(f"Maior: {maior}\nMeio: {meio}\nMenor: {menor}") print para debug


print(f"Crescente: {menor}, {meio}, {maior}\nDecrescente: {maior}, {meio}, {menor}")

