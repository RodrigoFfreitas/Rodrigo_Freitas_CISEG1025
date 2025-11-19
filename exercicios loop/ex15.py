
i = 0

while i <= 255:
    print(f"{i} - {chr(i)}")

    i += 1
    
    if i % 20 == 0:
        ask=input("Deseja continuar? (S/N): ")
        if ask.lower() == "s":
            continue
        else:
            break
    

