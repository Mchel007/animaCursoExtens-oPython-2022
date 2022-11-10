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
  imposto = preco_produto * 0.05
  return imposto

#calculando imposto:
preco = 299
imposto = calcular_imposto(preco)
print(imposto)

  








