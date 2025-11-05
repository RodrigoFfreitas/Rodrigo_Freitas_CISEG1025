# 1 minuto tem 60 segundos
# 1 hora tem 3600 segundos

userinput=0
segundos=0
minutos=0
horas=0

userinput=int(input("Insira os segundos "))



if userinput >= 0:
    if userinput >= 3600:
        horas = userinput // 3600
        userinput = userinput - (horas * 3600)

    if userinput >= 60:
        minutos = userinput // 60
        userinput = userinput - (minutos * 60)

    if userinput < 60:
        segundos = userinput
else:
    print("O valor inserido é inválido.")

print(f"{horas} Hora(s), {minutos} Minuto(s), {segundos} Segundo(s)")