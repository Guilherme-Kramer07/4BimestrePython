
#criando um vetor
notas= []

#criando a variável média
media = 0

for i in range (5):
    notaUnitaria = float(input("digite a nota"))
    notas.append(notaUnitaria)
    #O append incrementa o valor 

#o item no vai ser quem irá passar por todos os itens do vetor, e vai colocar dentro da media que irá somando item por item até finalizar o valor do item
for nota in notas:
    media = media+nota

media = media/5

print(media)