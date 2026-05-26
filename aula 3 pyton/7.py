def desconto(a,b):
    if b == 'PIX':
        valor = a * 0.9
    else:
        parcelamento = int(input('Quantidade de parcelas: '))
        if parcelamento <=3:
            valor = a/parcelamento
        else:
            valor = a*1.5/parcelamento
    return(valor)

total = float(input('Valor do produto: '))
pag = str(input('Forma de pagamento:(pix ou cartão): '))
cor_pag = pag.upper()
retorno = desconto(total,cor_pag)
print('O valor a ser pago é', retorno)
                    
                    

