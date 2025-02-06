numeros =[]

for i in range(10):
    numUnitario = float(input("digite um número"))
    numeros.append(numUnitario)

posicao = 0

for i in range(10):
    if numeros[posicao]< numeros[i]:
        posicao=i


print(f"A posição do maior número no vetor é: {posicao}")