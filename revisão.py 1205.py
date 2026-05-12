#a = 10
#b = 20
#a, b = 10,20
#print(a+b)
#o que são váriaveis 
#lista = ["Vanessao", "Carlota", "Enzo do pix"]

x = input("Digite seu nome: \n")

if x in lista:
    print("usuario encontrado")
else: 
    print("usuario não encontrado")    
#--------------------------------------
#idade = int(input("Digite sua idade:"))

#if idade >=16:
 #   print("você pode votar!")
#else:
 #   print("Você não pode votar")

idade = int(input("Digite sua idade:"))

if idade <=16:
   print("Não pode votar")
elif idade >=18 and idade <70:

  print("voto obrigratório")
else:
     print("Voto opicional")
#--------------------------------------
estoque = ["chevy", "Fiat", "peugeot", "volkswagem", "Lexus", "Ferrari"] 
preco_loja = [1000, 500, 1.99, 20000, 60000, 90000]

loja_barato = []
loja_caro = []

for i in range(len(preco_loja)):
    if preco_loja[i] <=20000:
     loja_barato.append(estoque[i])

    else:
        loja_caro.append(estoque[i])
        
print(loja_barato)
print(loja_caro)
