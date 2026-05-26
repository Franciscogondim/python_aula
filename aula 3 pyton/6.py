def comissao(a):
    if a >= 10000:
        comisao = float(a*0.1)
    else:
        comisao = 0
    return(comisao)



valor = float(input('Valor de vendas: '))
retorno = comissao(valor)
print(f"A comissão recebida é {retorno}")

