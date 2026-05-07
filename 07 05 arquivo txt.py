arquivo = open("revisao.txt", "a", encoding="utf-8")
arquivo.write("A gomes é top")
arquivo.close()

print("arquivo criado com sucesso!!!")

with open("arquivo_revisao.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("A Gomes é divina")
    print("arquivo criado com sucesso")
