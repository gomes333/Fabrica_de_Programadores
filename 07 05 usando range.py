numero = int(input("Digite um número: ")) # está usando um int e o input para digitar um número 
inicio = int(input("Digite o inicio da tabuada: "))# está usando o int e o input para marcar o inicio de uma tabuada 
fim = int(input("Digite o fim da tabuada: "))# está usando o int e o input para marcar o fim de uma tabuada

for i in range(inicio, fim + 1):
    print(f"{numero} x {i} = {numero * i} ")
