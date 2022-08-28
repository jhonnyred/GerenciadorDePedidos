import datetime
import os
import json

pedidos = dict()
historico = dict()
a = ' '
b = 60 * a

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

historico = uplo('historico.json', historico)
pedidos = uplo('pedidos.json', pedidos)


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
    w = input(b + '(1) Criar pedido\n' + b + '(2) Consultar pedido\n' + b + '(3) Consultar pedidos em andamento\n' + b + '(4) Remover pedido\n' + b + '(5) Concluir pedido\n' + b + '(6) Histórico\n' + b + '(Q) Sair\n' + b + '==>  ').upper()
    

    if w == '1':

        pula_linha(9)
        pedi['numero'] = input(b +'NUMERO do pedido: ')
        pedi['nome'] = input(b +'NOME do pedido: ').upper()
        pedi['telefone'] = input(b +'TELEFONE do pedido: ')
        pedi['pecas'] = input(b +'Número de PEÇAS: ')
        pedi['descricao'] = input(b +'DESCRIÇÃO do pedido: ')
        pedi['entrega'] = input(b +'ENTREGA do pedido: ')
        pedi['unitario'] = input(b +'VALOR UNITARIO do pedido: ')
        pedi['pagamento'] = input(b +'Qual a forma de PAGAMENTO: ')
        pedi['data'] = datetime.datetime.now().strftime('%d/%m/%y')
        pedi['total'] = float(pedi['unitario'])*int(pedi['pecas'])
        pedidos[pedi['numero']] = pedi
        pula_linha(9)
        for k,v in pedi.items():
                    print(b, k +': ' +str(v))
        l = input('\n' + b + 'Aperte ENTER para voltar')
        down(pedidos, 'pedidos.json')
    

    elif w == '2':

        pula_linha(10)
        w = input(b +'NUMERO, NOME ou TELEFONE do pedido \n' + b + ' ==>  ').upper()
        pedi = dict()
        encon = False
        for key in pedidos:
            pedi = pedidos[key]
            if w in pedi.values():
                for k,v in pedi.items():
                    print(b, k +': ' +str(v))
                    encon = True
            elif w not in pedi.values() and encon == False: 
                pula_linha(10)  
                print(b +'Não foi possível encontrar esse pedido, consulte os pedidos em andamento se necessário')
                break
        l = input('\n' + b + 'Aperte ENTER para voltar')



    elif w == '3':

        pula_linha(0)
        for key in pedidos:
            pedi = pedidos[key]
            print(pedi)
            print('\n')
        l = input('\n  Aperte ENTER para voltar')

    elif w == '4':

        pula_linha(10)
        w = input(b+'NUMERO do pedido que deseja remover \n' + b + ' ==>  ').upper()
        del pedidos[w]


    elif w == '5':

        pula_linha(10)
        w = input(b +'NUMERO do pedido concluído \n' +b +' ==>  ').upper()
        try:
            historico[w] = pedidos[w]
            del pedidos[w]
            l = input('\n' +b  +'Aperte ENTER para voltar')
            down(historico, 'historico.json')
        except:
            print(b +'Número invalido')
            l = input('\n' +b  +'Aperte ENTER para voltar')


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