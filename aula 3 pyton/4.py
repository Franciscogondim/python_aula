def salarioliq(a,b):
    total = float(a-(a*b))
    return(total)
bruto = float(input('Salário bruto: '))
desconto = float(input('Desconto: '))
desconto_real = float(desconto/100)
liq = salarioliq(bruto,desconto_real)
print(liq)