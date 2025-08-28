status = input("Digite o status do pedido: ")

match status:
    case "recebido":
        print("Seu pedido foi recebido.")
    case "em_preparacao":
        print("Seu pedido está em preparação.")
    case "em_entrega":
        print("Seu pedido está a caminho.")
    case "entregue":
        print("Seu pedido foi entregue.")
    case _:
        print("Status não identificado.")
