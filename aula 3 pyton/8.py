def salario_liq(a,b):
    sala_liq = a-(a*b)
    if sala_liq <= 2500:
        classe = 'Classe E'
    elif sala_liq >2500 and sala_liq <= 7000:
        classe = 'Classe D'
    elif sala_liq > 7000 and sala_liq<=15000:
        classe = 'Classe C'
    elif sala_liq >15000 and sala_liq<=25000:
        classe = 'Classe B'
    else:
        classe = 'Classe D'
    return(sala_liq,classe)
salario_bruto = float(input('Salario Bruto: '))
desconto = int(input('Valor do desconto: '))
desconto_real = desconto/100    
resultado = salario_liq(salario_bruto,desconto_real)
print('Seu salario liquido é',resultado[0],'e sua classe é',resultado[1])
