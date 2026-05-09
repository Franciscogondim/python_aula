n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))

media = float((n1 + n2)/2)

if media >= 7:
    print('Aprovado')
elif media < 4:
    print('Reprovado')
else:
    print('Final')

if media >= float(9):
    print('A')
elif media >= float(7) and media < float(9):
    print('B')
elif media >= float(4) and media < float(7):
    print('C')
else:
    print('D')



