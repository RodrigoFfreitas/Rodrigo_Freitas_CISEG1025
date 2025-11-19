num=int(input("Insira um numero inteiro: "))
i=1
ndivisores=0

while i <= num:
    if num % i == 0:
        ndivisores += 1
    i += 1

print(f"O numero {num} tem {ndivisores} divisores no total")
