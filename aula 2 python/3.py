soma = 0
while True:
    valor = int(input('Valor do produto: '))
    if valor != 0:
        soma += valor
        print(soma)
    else:
        break