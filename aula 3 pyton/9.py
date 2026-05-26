def calcular_media(a,b):
    media = (a+b)/2
    if media >=7:
        resultado = "Aprovado"
    elif media <4:
        resultado = "Reprovado"
    else:
        resultado = "Final"
    return(media,resultado)
qntd = int(input('Quantas vezes deseja repetir: '))
for i in range(qntd):
    a = int(input('Primeira Nota: '))
    b = int(input('Segunda Nota: '))
    fim = calcular_media(a,b)
    print('Média:', fim[0])
    print('Situação:', fim[1])
    print('==================')