contador = 0
while contador <15:
    contador = contador +1
    arquivo = open("arquivo.x", "a", encoding="utf-8")
    nome = input("Digite seu nome: \n")
    arquivo.write(f"\nCidade:{nome}\n")

arquivo.close()
