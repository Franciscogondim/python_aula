
while True:
    print("MENU")
    print("Aluno - opção 1")
    print("Professor - opção 2")
    print("Financeiro - opção 3")
    opcao = str(input('Escolha uma opção: '))
    print('-------------------------------------')
    match opcao:
        case str('1'):
            nome = str(input('Seu nome: '))
            n1 = float(input('Sua primeira nota: '))
            n2 = float(input('Sua segunda nota: '))
            media = float((n1+n2)/2)
            if media >= 70:
                print(f"Você esta aprovado e sua media foi {media}")
            elif media <= 60 and media >= 40:
                print(f"Você esta de recuperação e sua media foi {media}")
            else:
                print(f"Você esta reprovado e sua media foi {media}")
            print('-------------------------------')
        case str('2'):
            nome = str(input('Seu nome: '))
            titulo = str(input('Sua Titulação: '))
            titulo_lower = titulo.lower()
            if titulo_lower == 'mestrado' or titulo_lower == 'doutorado':
                print("Você pode realiza e orientar projetos")
            elif titulo_lower == 'graduação':
                print('Você pode ministrar apenas aulas básicas')
            else:
                print('Opção inválida')
            print('-------------------------------')
        case str('3'):
            print('Aluno - opção 1')
            print('Professor - opção 2')
            categoria = int(input('Sua opção: '))
            print('-------------------------------')
            match categoria:
                case 1: 
                    print('O valor da mensalidade é 700 reais')
                    print('Qual a forma de pagamento?: ')
                    print('Débito - opção 1')
                    print('Crédito - opção 2')
                    print('Dinheiro - opção 3')
                    pag = int(input('Opção: '))
                    print('-------------------------------')
                    match pag:
                        case 1:
                            print('insira o cartão')
                        case 2: 
                            print('insira o cartão')
                        case 3:
                            din = float(input('Quanto será pago: '))
                            if din > 700:
                                troco = din - 700
                                print(f"Seu troco é {troco}")
                            elif din < 700:
                                print('Valor insuficiente')
                            else:
                                print('Obrigado!!')
                        case _:
                                print('Opção inválida')
                    
                case 2:
                    ha = float(input('Valor da hora aula: '))
                    hx = float(input('Quantidade de horas extras: '))
                    vha = float(160 *ha)
                    vhx = float(hx*(ha+(ha*(50/100))))
                    total = float(vha + vhx)
                    print(f"Seu salario é  de {total} reais")
                case _:
                    print('Opção inválida') 
            print('-------------------------------')
        case _:
            print('Opção inválida')
            break

