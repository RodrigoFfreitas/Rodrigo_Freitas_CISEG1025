num1 = 0
num2 = 0
num3 = 0
maior=0
menor=0


num1=int(input('Insira um numero inteiro: '))
num2=int(input('Insira outro numero inteiro: '))
num3=int(input('Insira o ultimo numero inteiro inteiro: '))


if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
else: 
    maior = num3
    

if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
else:
    menor = num3
    
print(f"Maior: {maior}\nMenor: {menor}")