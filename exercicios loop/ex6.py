""" nprimos=0
num = 2
i = 2

while nprimos <= 10:
    if num % i == 0:
        print(f"{num} não é primo")
        num =+ 1
    else:
        print(f"{num} é primo")
        nprimos =+ 1
        i =+ 1 """
        
        
num = 3
nprimo = 1
list_primo = [2]


while nprimo < 10:
    i = 2
    primo = True

    while i < num:
        if num % i == 0:
            primo = False
            break
        i += 1

    if primo == True:
        list_primo.append(num)
        nprimo += 1

    num += 1

print(list_primo)

        