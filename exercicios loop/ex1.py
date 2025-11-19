npar=0
nimpar=0
i=0

while npar <= 30 and nimpar <= 30:
    if i % 2 == 0:
        print(f"O número {i} é par")
        npar += 1
        i += 1
    else:
        print(f"O número {i} é impar")
        nimpar += 1
        i += 1
