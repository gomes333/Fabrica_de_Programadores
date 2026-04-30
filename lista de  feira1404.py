print("------Lista de Feira------")

lista = ["abacaxi"]

opcao = input("Digite uma fruta que você queira procurar: \n\n")

if opcao in lista:
    print(f"A fruta {opcao} está na lista!!!")

else:
    nova_fruta = ("Você quer adicionar uma nova fruta a lista da feira? (sim/não)\n\n").lower
    if nova_fruta == "sim":
        nova_lista = input("Digite o nome da fruta que queira adicionar a lista: \n")
        lista.append(nova_lista)
        print(f"A fruta {nova_lista} está adicionada a lista")

    else:
        print("Encerrando...\n\n")
