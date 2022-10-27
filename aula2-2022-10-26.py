#comando input quero permintir que o usuario digite algo

#comando de saida... exibir saída

nome = input("digite seu nome: ")
idade= int(input("qual sua idade: "))
print(f"seu nome é {nome} e sua idade é {idade}\n")

#e se eu quisesse mostrar o dobro d idade informada
dobro = idade * 2
print(f"o dobro da idade é {dobro}\n")
#estrutura conicional o famoso if
#se a pessoa for maior de idade mostre "vc é maior de idade ja pode beber e dirigir"
if idade >= 18:
  print ("você é maior de idade! \n")
 
else:
  print("você é jovem ainda, Robin.\n")


  #se eu quisesse  perguntar o genero m e f
#mostre (.. e precisa prestar o serviço militar obrigatório )
genero = input("Informe o genero M=Masculino, f=feminino e o=outros: \n")
if idade >=18 and genero == "M":
  print("E você precisa/precisou se alistar no exercito")
