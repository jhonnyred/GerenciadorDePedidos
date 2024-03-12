import datetime
import os
import json

pedidos = dict()
historico = dict()

a = ' '
space = 60 * a

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def uplo(arquivo, dicio):
    with open(arquivo, 'r') as file:
        dicio = json.load(file)
    return dicio

def down(dicio, arquivo):
    with open(arquivo, 'w') as file:
        json.dump(dicio, file)
    return dicio

def pula_linha(a):
    os.system('cls')
    while a != 0:
        print('\n')
        a = a - 1

pedidos = uplo('pedidos.json', pedidos)
historico = uplo('historico.json', historico)


while True:
    pedi = dict()
    pedi['numero'] = None
    pedi['nome'] = None
    pedi['telefone'] = None
    pedi['pecas'] = None
    pedi['descricao'] = None
    pedi['data'] = None
    pedi['entrega'] = None
    pedi['unitario'] = None
    pedi['total'] = 0
    pedi['pagamento'] = None

    pula_linha(9)
    w = input(space + '(1) Criar pedido\n' + space + '(2) Consultar pedido\n' + space + '(3) Consultar pedidos em andamento\n' + space + '(4) Remover pedido\n' + space + '(5) Concluir pedido\n' + space + '(6) Histórico\n' + space + '(Q) Sair\n' + space + '==>  ').upper()
    

    if w == '1':

        pula_linha(9)
        pedi['numero'] = input(space +'NUMERO do pedido: ')
        check = pedi['numero'].isdigit()
        while not check:
               pula_linha(9)
               pedi['numero'] = input(space +'NUMERO inválido, digite novamente: ')
               check = pedi['numero'].isdigit()
        
        pula_linha(9)
        print(space +'NUMERO do pedido: ' +pedi['numero'])

        pedi['nome'] = input(space +'NOME do pedido: ').upper()
        pedi['telefone'] = input(space +'TELEFONE do pedido: ')
        
        pedi['pecas'] = input(space +'Número de PEÇAS: ')
        check = pedi['pecas'].isdigit()
        while not check:
            pula_linha(9)
            pedi['pecas'] = input(space +'Número de PEÇAS inválido, digite novamente usando somente números: ')
            check = pedi['pecas'].isdigit()
        
        pula_linha(9)
        print(space +'NUMERO do pedido: ' +pedi['numero'])

        print(space +'NOME do pedido: ' +pedi['nome'])
        print(space +'TELEFONE do pedido: ' +pedi['telefone'])

        print(space +'Número de PEÇAS: ' +pedi['pecas'])
        pedi['descricao'] = input(space +'DESCRIÇÃO do pedido: ') 

        pedi['entrega'] = input(space +'ENTREGA do pedido: ')
        
        pedi['unitario'] = input(space +'VALOR UNITARIO do pedido: ')
        check = isfloat(pedi['unitario'])
        while not check:
            pula_linha(9)
            pedi['unitario'] = input(space +'Valor inválido, lembre-se de trocar vírgulas por pontos: ')
            check = isfloat(pedi['unitario'])

        pula_linha(9)
        print(space +'NUMERO do pedido: ' +pedi['numero'])

        print(space +'NOME do pedido: ' +pedi['nome'])
        print(space +'TELEFONE do pedido: ' +pedi['telefone'])

        print(space +'Número de PEÇAS: ' +pedi['pecas'])
        print(space +'DESCRIÇÃO do pedido: ' +pedi['descricao'])

        print(space +'ENTREGA do pedido: ' +pedi['entrega'])
        print(space +'VALOR UNITÁRIO do pedido: ' +pedi['unitario'])
        
        pedi['pagamento'] = input(space +'Qual a forma de PAGAMENTO: ')
        pedi['data'] = datetime.datetime.now().strftime('%d/%m/%y')
        
        pedi['total'] = float(pedi['unitario'])*int(pedi['pecas'])
        pedidos[pedi['numero']] = pedi
        
        pula_linha(9)
        for k,v in pedi.items():
                    print(space, k +': ' +str(v))
        l = input('\n' + space + 'Aperte ENTER para voltar')
        down(pedidos, 'pedidos.json')
    

    elif w == '2':

        pula_linha(10)
        w = input(space +'NUMERO, NOME ou TELEFONE do pedido \n' + space + ' ==>  ').upper()
        pedi = dict()
        encon = False
        for key in pedidos:
            pedi = pedidos[key]
            if w in pedi.values():
                pula_linha(9)
                for k,v in pedi.items():
                    print(space, k +': ' +str(v))
                encon = True  
        if encon == False:
            print(space +'Não foi possível encontrar esse pedido, consulte os pedidos em andamento se necessário')
        l = input('\n' + space + 'Aperte ENTER para voltar')



    elif w == '3':

        pula_linha(0)
        print(space +'Numero | Nome | Telefone | Descrição')
        print(space +'________________________________________________')
        for key in pedidos:
            pedi = pedidos[key]
            print(space +pedi['numero'] +'   ' +pedi['nome'] +'   ' +pedi['telefone'] +'   ' +pedi['descricao'])
            print(space +'________________________________________________')
        l = input('\n' +space +'Aperte ENTER para voltar')

    elif w == '4':

        pula_linha(10)
        w = input(space+'NUMERO do pedido que deseja remover \n' + space + ' ==>  ').upper()
        try:
            del pedidos[w]
            down(pedidos, 'pedidos.json')
        except:
            print(space +'Número invalido')
            l = input('\n' +space  +'Aperte ENTER para voltar')


    elif w == '5':

        pula_linha(10)
        w = input(space +'NUMERO do pedido concluído \n' +space +' ==>  ').upper()
        try:
            historico[w] = pedidos[w]
            del pedidos[w]
            l = input('\n' +space  +'Aperte ENTER para voltar')
            down(historico, 'historico.json')
        except:
            print(space +'Número invalido')
            l = input('\n' +space  +'Aperte ENTER para voltar')


    elif w == '6':

        pula_linha(0)
        for key in historico:
            pedi = historico[key]
            print(pedi)
            print('\n')
        l = input('\n  Aperte ENTER para voltar')  


    elif w == 'Q':

        down(historico, 'historico.json')
        down(pedidos, 'pedidos.json')
        break
