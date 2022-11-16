#pede nome e nota de 0 a 10, se tirar 10 mostre (vc é brabo)
nome = input("Qual seu nome ?: ")
nota = float(input("Qual a nota? "))
if (nota==10):
  print(f" {nome}, Você é brabo")
elif (nota >= 6 and nota<=10):
  print(f"{nome}, bom trabalho!")
else:
  print(" vamo melhorar ae")