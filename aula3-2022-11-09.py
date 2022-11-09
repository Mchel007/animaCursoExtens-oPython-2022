print ( 'inicio da aula 3\n')

contador = 1

#estruturas de repetição
while(contador <= 10 ):
  print ( contador )
  contador = contador +1
  

#laço for
fruta = "morango" 
print ( fruta )

fruta1 = "morango"
fruta2 = "laranja"
fruta3 = "banana"

#lista
frutas = ["morango", "laranja", "banana"] 
  
#exibir apenas a fruta3//morango=0/laranja=1/banana=2 pq começa contando de 0 ( )
print (frutas[2])
print (frutas [1])

#exebir quantas frutas tem na lista

print (len (frutas))
#incluir uma fruta a patir da lista pronta
frutas.append("manga") 
print (len(frutas))
print ( frutas)

print ("\nExemplo das frutas com while:\n")
frutas.append ("uva")

i=0
while(i<len(frutas) ):
  print (frutas[i])
  i=i+1










