contador = 0
while contador <10:
    contador = contador +1
    arquivo = open("revisao.txt", "a", encoding="utf-8")
    empresa = input("Digite sua empresa: \n")
    arquivo.write(f"\nCidade:{empresa}\n")

arquivo.close()
