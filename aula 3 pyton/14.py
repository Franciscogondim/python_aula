adicionados = []
listados = []
removidos = []

def calcular_media(n1, n2):
    media = (n1 + n2) / 2

    adicionados.append(media)

    if media > 70:
        return "Aprovado"
    elif media < 40:
        return "Reprovado"
    else:
        return "Final"


resultado = calcular_media(80, 90)

listados.append(resultado)

print("Resultado:", resultado)

removidos.append(adicionados.pop(0))

print("Adicionados:", adicionados)
print("Listados:", listados)
print("Removidos:", removidos)