adicionados = []
listados = []
removidos = []

def desconto(valor, pagamento, parcelas=1):

    adicionados.append(valor)

    if pagamento == "pix":
        valor_final = valor - (valor * 0.10)

    elif pagamento == "cartao":
        if parcelas <= 3:
            valor_final = valor
        else:
            valor_final = valor + (valor * 0.05)

    return valor_final


resultado = desconto(1000, "cartao", 5)

listados.append(resultado)

print("Valor final:", resultado)

removidos.append(adicionados.pop(0))

print("Adicionados:", adicionados)
print("Listados:", listados)
print("Removidos:", removidos)