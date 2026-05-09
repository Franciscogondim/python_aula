quant = int(input('Quantidade de maçãs'))

if quant < int(12):
    maca= float(1.30)
    preco = float(maca*quant)
else:
    maca= int(1)
    preco = int(maca*quant)
pag = str(input('Qual a forma de pagamento?:(Débito,Crédito,Dinheiro) '))

if pag == str('Débito') or pag == str('débito') or pag ==str('Crédito') or pag == str('crédito'):
    print('Insira o cartão')
else:
    din = float(input('Dinheiro entregue: '))
    troco = float(din - preco)
    if troco < float(0):
        print('invalido')
    else:
        print('Seu troco é:', troco)
    