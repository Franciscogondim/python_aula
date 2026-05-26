produto = []
qntd = []
valor = []
print('cadastrar - opção 1')
print('Ver cadastros - opção 2')
print('Remover cadastro - opção 3')
print('Parar - opção 0')
print('==================================')
opcao = int(input('Opção: '))
while opcao != 0:
    match opcao:
        case 1:
            cadastrado = str(input('Produto: '))
            quantidade = int(input('Quantidade: '))
            dinheiro = float(input('Valor: '))
            produto.append(cadastrado)
            qntd.append(quantidade)
            valor.append(dinheiro)
        case 2:
            for nome,quant,renda in zip(produto,qntd,valor):
                print(f'Produto: {nome} | Quantidade: {quant} | Valor: {renda}')
        case 3:
            nome_remover = str(input('Produto que deseja remover: '))
            if nome_remover in produto:
                indice = produto.index(nome_remover)
                produto.pop(indice)
                qntd.pop(indice)
                valor.pop(indice)
        case 0:
                break
        case _:
                print('Opção inválida')

    print('==================================')
    print('cadastrar - opção 1')
    print('Ver cadastros - opção 2')
    print('Remover cadastro - opção 3')
    print('Parar - opção 0')
    print('==================================')
    opcao = int(input('Opção: '))