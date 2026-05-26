adicionados = []
listados = []
removidos = []

def salario_liquido(salario, desconto):

    liquido = salario - desconto

    adicionados.append(liquido)

    if liquido <= 2500:
        classe = "Classe E"
    elif liquido <= 7000:
        classe = "Classe D"
    elif liquido <= 15000:
        classe = "Classe C"
    elif liquido <= 25000:
        classe = "Classe B"
    else:
        classe = "Classe A"

    return liquido, classe


resultado = salario_liquido(10000, 2000)

listados.append(resultado)

print("Resultado:", resultado)

removidos.append(adicionados.pop(0))

print("Adicionados:", adicionados)
print("Listados:", listados)
print("Removidos:", removidos)