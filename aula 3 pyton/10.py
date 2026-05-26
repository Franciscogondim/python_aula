def comissao(a):
    if a >= 10000:
        comisao = float(a*0.1)
    else:
        comisao = 0
    return(comisao)

qntd = int(input('Quantas vezes deseja repetir?: '))
for i in range(qntd):
    valor = float(input('Valor da venda: '))
    retorno = comissao(valor)
    print(f"A comissão recebida é {retorno}")

