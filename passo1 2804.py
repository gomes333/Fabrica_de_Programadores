arquivo = open("arquivo.txt", "a", encoding="utf-8")
arquivo.write("\n você é top")
arquivo.close()

nome = input("Digite seu nome: \n")
nota = int(input("Digite a nota: \ n"))
arquivo.write("-"*20)
arquivo.write(f"\nAluno:{nome}\n")
arquivo.write(f"\nNota:{nota}\n")
arquivo.write("-"*20)

arquivo.close()
