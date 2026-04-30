lista = ["Junior", "Vanessa"] #lista com cadastro pessoal

usuario = input("Digite seu usuário: \n") #uma variavel usando nome de usuário com input

print("------INICIO------ \n") #titulo que indica inicio 
if usuario in lista: # indica "se" ou "em"
    print("Login bem-sucedido!!!\n") #mostra se deu certo 

else:# indica outra
    print(f"Usuário {usuario} não existe!!!\n") # mostra que o usuário não existe 
print("------FIM------ \n") #titulo que indica fim


 