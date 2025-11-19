num=int(input("Insira um numero inteiro: "))
i=(num-1)

while i >= 1:
    soma = num + i
    subt = num - i
    mult = num * i
    divi = num / i
    
    print(f"{num} + {i} = {soma}")
    print(f"{num} - {i} = {subt}")
    print(f"{num} x {i} = {mult}")
    print(f"{num} / {i} = {divi}")
    
    i -= 1