import datetime
import os
import platform
import json

# Inicialização dos dicionários
pedidos = dict()
historico = dict()
balanco = str()
entrada = str()
saida = str()


# Eixo Y (Y axis)
Yaxis = 60 * ' '


# Eixo X (X axis)
def Xaxis(numero):
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

    for i in range(numero):
        print('\n')
        numero -= 1


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


#  Upload JSON
def uplo(arquivo, dicio):
    with open(arquivo, 'r') as file:
        dicio = json.load(file)
    return dicio


# Download JSON
def down(dicio, arquivo):
    with open(arquivo, 'w') as file:
        json.dump(dicio, file)
    return dicio


# Download TXT
def downtxt(arquivo, variavel, status, pagamento):
        with open(arquivo, 'r') as text_file:
            if status == 'entrada':
                alldata = 'R$' + str(variavel).replace('.', ',') + pagamento + datetime.datetime.now().strftime('   %d/%m/%y  %H:%M ') + 'ENTRADA\n'        
            else:
                alldata = 'R$' + str(variavel).replace('.', ',') + pagamento + datetime.datetime.now().strftime('   %d/%m/%y  %H:%M ') + 'SAÍDA\n'        
        
            for line in text_file:
                alldata = alldata + line

            with open(arquivo, 'w') as text_file2:
                text_file2.write(alldata)


# Tranferência de dados para os dicionários
pedidos = uplo('pedidos.json', pedidos)
historico = uplo('historico.json', historico)
with open('balanco.txt', 'r') as file:
    for line in file:
        a = line.find('$')
        b = line.find(' ')
        balanco = balanco + line[a+1:b].rstrip().replace(',', '.')
        balanco = float(balanco)
        break


# Main
while True:

    #Dicionário molde
    pedi = dict()
    pedi['numero'] = None
    pedi['nome'] = None
    pedi['telefone'] = None
    pedi['pecas'] = None
    pedi['descricao'] = None
    pedi['data'] = None
    pedi['entrega'] = None
    pedi['total'] = 0
    pedi['pagamento'] = None


# MENU
    Xaxis(5)
    w = input(Yaxis+ 'Balanço de caixa: ' + str(balanco) + '\n\n\n' + Yaxis+ 'CAIXA\n\n' + Yaxis+ '(E) Entradas\n' + Yaxis+ '(S) Saídas\n\n' + Yaxis+ 'GERENCIAMENTO DE PEDIDO\n\n' + Yaxis+ '(1) Criar pedido\n' + Yaxis+ '(2) Editar pedido\n' + Yaxis+ '(3) Consultar pedido\n' + Yaxis+ '(4) Consultar pedidos em andamento\n' + Yaxis+ '(5) Remover pedido\n' + Yaxis+ '(6) Concluir pedido\n\n' + Yaxis+ 'HISTÓRICOS\n\n' + Yaxis+ '(7) Pedidos\n'+ Yaxis+'(8) Entradas\n'+ Yaxis+ '(9) Saídas\n' + Yaxis+ '(0) Balanço\n\n' + Yaxis+ '(Q) Sair\n' + Yaxis+ '==>  ').upper()

# ENTRADAS
    if w == 'E':

        Xaxis(9)
        entrada = input(Yaxis + 'R$ ').replace(',', '.')
        pagamento = '  ' + input(Yaxis + 'Forma de pagamento: ')

        Xaxis(9)
        print(Yaxis+ 'R$'+ entrada + pagamento + '\n' +Yaxis+ 'pressione E para confirmar ou Q para cancelar operação')
        b = input('\n' +Yaxis+ '==> ').upper()

        if b == 'E':
            balanco = balanco + float(entrada)
            #DOWNLOAD HIST. ENTRADAS
            downtxt('entrada.txt', entrada, 'entrada', pagamento)

            #DOWNLOAD HIST. BALANÇO
            downtxt('balanco.txt', balanco, 'entrada', pagamento)
        else:
            continue


# SAÍDAS
    elif w == 'S':

        Xaxis(9)
        saida = input(Yaxis + 'R$ ').replace(',', '.')
        pagamento = '  ' + input(Yaxis + 'Forma de pagamento: ')

        Xaxis(9)
        print(Yaxis+ 'R$'+ saida + pagamento + '\n' +Yaxis+ 'pressione E para confirmar ou Q para cancelar operação')
        b = input('\n' +Yaxis+ '==> ').upper()

        if b == 'E':
            balanco = balanco + float(saida) 
            #DOWNLOAD HIST. SAÍDAS
            downtxt('saida.txt', saida, 'saida', pagamento)

            #DOWNLOAD HIST. BALANCO
            downtxt('balanco.txt', balanco, 'saida', pagamento)
        else:
            continue


# CRIAR PEDIDO
    elif w == '1':

        Xaxis(9)
        pedi['numero'] = input(Yaxis +'NUMERO do pedido: ')
        check = pedi['numero'].isdigit()
        while not check:
               Xaxis(9)
               pedi['numero'] = input(Yaxis +'NUMERO inválido, digite novamente: ')
               check = pedi['numero'].isdigit()
        
        Xaxis(9)
        print(Yaxis +'NUMERO do pedido: ' +pedi['numero'])

        pedi['nome'] = input(Yaxis +'NOME do pedido: ').upper()
        pedi['telefone'] = input(Yaxis +'TELEFONE do pedido: ')
        
        pedi['pecas'] = input(Yaxis +'Número de PEÇAS: ')
        check = pedi['pecas'].isdigit()
        while not check:
            Xaxis(9)
            pedi['pecas'] = input(Yaxis +'Número de PEÇAS inválido, digite novamente usando somente números inteiros: ')
            check = pedi['pecas'].isdigit()
        
        Xaxis(9)
        print(Yaxis +'NUMERO do pedido: ' +pedi['numero'])

        print(Yaxis +'NOME do pedido: ' +pedi['nome'])
        print(Yaxis +'TELEFONE do pedido: ' +pedi['telefone'])

        print(Yaxis +'Número de PEÇAS: ' +pedi['pecas'])
        pedi['descricao'] = input(Yaxis +'DESCRIÇÃO do pedido: ') 

        pedi['entrega'] = input(Yaxis +'DATA DE ENTREGA do pedido: ')
        
        pedi['pagamento'] = input(Yaxis +'Qual a forma de PAGAMENTO: ')
        pedi['total'] = input(Yaxis + 'VALOR TOTAL do pedido: ')
        pedi['data'] = datetime.datetime.now().strftime('%d/%m/%y')
        
        pedidos[pedi['numero']] = pedi
        
        Xaxis(9)
        for k,v in pedi.items():
                    print(Yaxis, k +': ' +str(v))
        l = input('\n' + Yaxis + 'Pressione ENTER para salvar e voltar')
        down(pedidos, 'pedidos.json')


# EDITAR PEDIDO
    elif w == '2':

        Xaxis(10)
        w = input(Yaxis +'Digite o NUMERO do pedido que deseja editar \n' +Yaxis +' ==>  ')
        
        if w in pedidos:
            pedi = pedidos[w].copy()

        #MENU DE EDIÇÃO
            
            done = False
            while done == False:
                Xaxis(8)
                print(Yaxis +'MENU EDIÇÃO')
                print(Yaxis +'(salve as alterações antes de sair do menu edição)\n')
                pedi['nome'] = pedi['nome'].upper()
                for key, value in pedi.items():
                    print(Yaxis + key +':', pedi[key])
                print('\n' +Yaxis +'[S] salvar [Q] sair')
                b = input(Yaxis +'Digite o item a ser editado \n' +Yaxis +' ==>  ').lower()

                if b == 'numero':
                    Xaxis(10)
                    print(Yaxis +'Não é possível alterar o número do pedido, se necessário crie outro pedido\n')
                    b = input(Yaxis +'Pressione ENTER para continuar')
                
                #SAVE
                elif b == 's':
                    pedidos[w] = pedi
                    b = input(Yaxis +'Salvo!\n' +Yaxis +'Pressione ENTER para continuar')
                    down(pedidos, 'pedidos.json')

                #QUIT
                elif b == 'q':
                    pedi = dict()
                    done = True
                
                #ALTERA
                elif b != 'q' or b != 's':
                    Xaxis(10)
                    if b in pedi:
                        print(f'{Yaxis}{b}: {pedi[b]}\n')
                        pedi[b] = input(Yaxis +' ==>  ').replace(',', '.')

                    else:
                        print(Yaxis +'Não foi possível encontrar este item\n')
                        b = input(Yaxis +'Pressione ENTER para voltar ao menu edição')
        
        else:
            print(Yaxis +'Não foi possível localizar o pedido\n')
            w = input(Yaxis +'Pressione ENTER para voltar')

# LOCALIZAR PEDIDO
    elif w == '3':

        Xaxis(10)
        w = input(Yaxis +'NUMERO, NOME ou TELEFONE do pedido \n' + Yaxis + ' ==>  ').upper()
        pedi = dict()
        encon = False
        
        for nume, info in pedidos.items():
            if w == nume:
                Xaxis(9)
                for k in info:
                    print(Yaxis, k  +':', info[k])
                encon = True
            elif w == info['nome']:
                Xaxis(9)
                for k in info:
                    print(Yaxis, k +':', info[k])
                encon = True
            elif w == info['telefone']:
                Xaxis(9)
                for k in info:
                    print(Yaxis, k +':', info[k])
                encon = True 
        
        if encon == False:
            print(Yaxis +'Não foi possível encontrar esse pedido, consulte os pedidos em andamento se necessário')
        l = input('\n' + Yaxis + 'Pressione ENTER para voltar')


# PEDIDOS EM ANDAMENTO
    elif w == '4':

        Xaxis(0)
        print(Yaxis +'Numero | Nome | Telefone | Descrição')
        print(Yaxis +'________________________________________________')
        for key in pedidos:
            pedi = pedidos[key]
            print(Yaxis +pedi['numero'] +'   ' +pedi['nome'] +'   ' +pedi['telefone'] +'   ' +pedi['descricao'])
            print(Yaxis +'________________________________________________')
        l = input('\n' +Yaxis +'Pressione ENTER para voltar')


# REMOVER PEDIDO
    elif w == '5':

        Xaxis(10)
        w = input(Yaxis+'NUMERO do pedido que deseja remover \n' + Yaxis + ' ==>  ').upper()
        try:
            del pedidos[w]
            down(pedidos, 'pedidos.json')
        except:
            print(Yaxis +'Número invalido')
            l = input('\n' +Yaxis  +'Pressione ENTER para voltar')


# CONCLUSÃO DE PEDIDO
    elif w == '6':

        Xaxis(10)
        w = input(Yaxis +'NUMERO do pedido concluído \n' +Yaxis +' ==>  ').upper()
        try:
            historico[w] = pedidos[w]
            del pedidos[w]
            l = input('\n' +Yaxis  +'Pressione ENTER para voltar')
            down(historico, 'historico.json')
        except:
            print(Yaxis +'Número invalido')
            l = input('\n' +Yaxis  +'Pressione ENTER para voltar')


# EXIBIÇÃO DO HISTÓRICO
    elif w == '7':

        Xaxis(0)
        for key in historico:
            pedi = historico[key]
            print(pedi)
            print('\n')
        l = input('\n  Pressione ENTER para voltar')


# HISTORICO ENTRADAS
    elif w == '8':

        Xaxis(0)
        with open('entrada.txt', 'r') as file:
            for line in file:
                print(Yaxis + line)

        enter = input('\n' +Yaxis+ 'Pressione ENTER para voltar')


#HISTORICO SAIDAS
    elif w == '9':

        Xaxis(0)
        with open('saida.txt', 'r') as file:
            for line in file:
                print(Yaxis + line)
        
        enter = input('\n' +Yaxis+ 'Pressione ENTER para voltar')

#HISTORICO BALANÇO
    elif w == '0':

        Xaxis(0)
        with open('balanco.txt', 'r') as file:
            for line in file:
                print(Yaxis + line)

        enter = input('\n' +Yaxis+ 'Pressione ENTER para voltar')


# FECHAR PROGRAMA
    elif w == 'Q':

        down(historico, 'historico.json')
        down(pedidos, 'pedidos.json')
        break
