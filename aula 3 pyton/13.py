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

soma = []
lanche = float(input('Preço do produto: '))
while lanche !=0:
    lanche = float(input('Preço do produto: '))
    soma.append(lanche)
total = sum(soma)
pag = str(input('Forma de pagamento:(pix ou cartão): '))
cor_pag = pag.upper()
retorno = desconto(total,cor_pag)
print('O valor a ser pago é', retorno)

