numeros =[]

for i in range(10):
    numUnitario = float(input("digite a nota"))
    numeros.append(numUnitario)

qtNeg = 0
somaPos = 0
for numUnitario in numeros:
    if numUnitario < 0:
        qtNeg += 1
    if numUnitario > 0:
        somaPos+= numUnitario

print(f'A soma dos positivos é: {somaPos} e a quantidade de negativos é: {qtNeg}')
