num=int(input("Insira um numero inteiro: "))
i=1
cont_opr = 0 

while i < num:
    soma = num + i
    subt = num - i
    mult = num * i
    divi = num / i
    
    print(f"{num} + {i} = {soma}")
    print(f"{num} - {i} = {subt}")
    print(f"{num} x {i} = {mult}")
    print(f"{num} / {i} = {divi}")
    
    cont_opr += 4
    
    i += 1

print(f"O total de operações efetuadas foi de: {cont_opr}")