operacao=""
num1=0.0
num2=0.0
resultado=0.0


print('Insira uma das seguinte Operações:\n- Soma\n- Subtração\n- Multiplicação\n- Divisão\n(Não utilize caracteres Especiais)')
operacao=input('')

num1=float(input('Insira o primeiro número da equação: '))
num2=float(input('Insira o segundo número da equação: '))

match operacao.lower():
    case "soma":
        resultado=num1+num2
        print(f"O resultado de {num1} + {num2} é {resultado}")
    case "subtracao":
        resultado=num1-num2
        print(f"O resultado de {num1} - {num2} é {resultado}")
    case "multiplicacao":
        resultado=num1*num2
        print(f"O resultado de {num1} x {num2} é {resultado}")
    case "divisao":
        resultado=num1/num2
        print(f"AO resultado de {num1} / {num2} é {resultado}")
    case _:
        print("Operação Invalida")
