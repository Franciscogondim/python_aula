def desconto(a,b):
    if b == 'PIX':
        valor = a-(a*0.1)
    else:
        parcelamento = int(input('Quantidade de parcelas: '))
        if parcelamento <=3:
            valor = a/parcelamento
        else:
            valor = a+(a*0.5*parcelamento)/parcelamento
    return(valor)
qntd = int(input('Quantidade de repetições: '))
for i in range(qntd):
    print(f'item {i+1}')
    total = float(input('Valor do produto: '))
    pag = str(input('Forma de pagamento:(pix ou cartão): '))
    cor_pag = pag.upper()
    retorno = desconto(total,cor_pag)
    print('O valor a ser pago é', retorno)