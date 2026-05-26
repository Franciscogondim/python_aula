def calcular_media(a,b):
    media = (a+b)/2
    if media >=7:
        resultado = "Aprovado"
    elif media <4:
        resultado = "Reprovado"
    else:
        resultado = "Final"
    return(media,resultado)
fim = calcular_media(5,5)
print('Média:', fim[0])
print('Situação:', fim[1])

        