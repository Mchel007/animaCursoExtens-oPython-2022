#criaçao de funções( )

preco = 1999.90

#calcular 5% do imposto, guardar variavel e imprimir na tela
imposto = preco * 0.05
print (imposto )

preco2 = 100
imposto2 = preco2 * 0.05
print (imposto2 )

#criar uma funçao calcular_imposto() que calcula um imposto de 5% e retorna
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.07
  return imposto

#calculando imposto:
preco = 299
imposto = calcular_imposto(preco)
print(f"essa funcao é (7%):{imposto}")

#imposto agr 7% ()

valores = [1.99, 24.50, 78.27, 1515.5]
#imposto desses quatro valores
for valor in valores:
  print (f"o imposto de {valor} é {calcular_imposto(valor)}")

  








