
status=""
delay=0

status=input('Insira o status do servidor: ')
delay=int(input('Insira o delay em milisegundos do servidor: '))


match status:
    case "ok" if delay > 200:        # se o status estiver ok e delay for superior a 200ms o server ta lento 
        print('Servidor lento')      # OBS: Tem de estar antes do "Servidor Ativo", pq se estiver depois, o python vai ignora-lo, 
    case "ok":
        print('Servidor Ativo!')
    case "erro":
        print("Servidor indisponivel")
    case _:
        print("Estado Desconhecido")
