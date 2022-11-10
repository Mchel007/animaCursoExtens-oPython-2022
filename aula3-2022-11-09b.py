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
print(f"essa funcao é (7%):\n{imposto}")

#imposto agr 7% ()

valores = [1.99, 24.50, 78.27, 1515.5]
#imposto desses quatro valores
for valor in valores:
  print (f"o imposto de {valor} é {calcular_imposto(valor)}")

  #Declarar um função calcula_imposto_aliquota() que recebe dois parâmetros: o preço do produto e a alíquota de imposto a ser aplicada e retorna o imposto calculado. Se a aliquota não for informada, utilize 7% como padrão.

def calcular_imposto_aliquota(valor, aliquota =7):
  imposto = valor * aliquota / 100
  return imposto
  
for valor in valores:
  print (f"o imposto de {valor} é:  {calcular_imposto_aliquota(valor)}")






