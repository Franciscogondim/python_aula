def desconto():
    a = float(input('Preço do produto: '))
    b = float(0.1)
    total = float(a-(a*b))
    return(total)

total = desconto()
print(total)

