conta = int(input('Número da conta: '))
saldo = float(input('Seu saldo:'))
debito = float(input('Seu debito: '))
credito = float(input('Seu Crédito: '))

saldoa = float(saldo - debito + credito)
print(saldoa)
if saldoa >= 0:
    
    print('Saldo Positivo')
else:
    print('Saldo Negativo')
