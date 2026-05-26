adicionados = []
listados = []
removidos = []

def comissao(vendas):

    adicionados.append(vendas)

    if vendas > 10000:
        return vendas * 0.10
    else:
        return 0


resultado = comissao(15000)

listados.append(resultado)

print("Comissão:", resultado)

removidos.append(adicionados.pop(0))

print("Adicionados:", adicionados)
print("Listados:", listados)
print("Removidos:", removidos)