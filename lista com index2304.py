lista_de_usuario = ["Felipe","Isadiva","Kauan"]
senha_do_usuario = ["F3lip3", "1s4d1v4","K4u4n"]

usuario = input("Digite seu usuario...\n")
senha = input("Digite sua senha\n") 

index_usuario = lista_de_usuario.index(usuario)
index_senha = senha_do_usuario.index(senha)

print(index_usuario)

if usuario in lista_de_usuario:
    index = lista_de_usuario.index(usuario)

    print("usuario existe")    
