cor = input("Digite a cor do semáforo (verde, amarelo, vermelho): ")

match cor:
    case "verde":
        print("Pode passar.")
    case "amarelo":
        print("Atenção, reduza a velocidade.")
    case "vermelho":
        print("Pare!")
    case _:
        print("Sinal inválido.")
