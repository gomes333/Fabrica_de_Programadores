print("------lista de nomes------")

nova_lista = ["Vanessa","Carla","Enzo","Gustavo"]
contador = 0
while contador <4:
    contador = contador +1
    lista = input("Digite o novo nome que você queira adicionar a lista: \n")
    nova_lista.append(lista)
    print(f"Os nomes {nova_lista} estão adicionados a lista")
    
