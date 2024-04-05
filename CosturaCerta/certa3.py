import datetime
import os
import json

# Abre 2 dicionários e 3 variáveis, aqui é onde estão armazenados todos os dicionários (pedidos para aqueles pedidos que não foram concluidos e historico para aqueles ja concluidos)
pedidos = dict()
historico = dict()
balanco = str()
entrada = str()
saida = str()


# Variáveis que possuem strings atribuidas para ajudar na formatação do menu
a = ' '
space = 60 * a


# Função necessária para a formatação do menu
def pula_linha(a):
    os.system('cls')
    while a != 0:
        print('\n')
        a = a - 1


# Aparentemente uma função dedicada a indentificar dados em formato float
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


# Função para faciltiar o upload de arquivos
def uplo(arquivo, dicio):
    with open(arquivo, 'r') as file:
        dicio = json.load(file)
    return dicio


# Funções para facilitar o download de arquivos
def down(dicio, arquivo):
    with open(arquivo, 'w') as file:
        json.dump(dicio, file)
    return dicio

def downtxt(arquivo, variavel):
    with open(arquivo, 'r') as text_file:
        alldata = 'R$' + str(variavel).replace('.', ',') + datetime.datetime.now().strftime('   %d/%m/%y  %H:%M\n')
        for line in text_file:
            alldata = alldata + line

        with open(arquivo, 'w') as text_file2:
            text_file2.write(alldata)


# Atribuição dos dados contidos nos arquivos aos respectivos dicionários e variáveis (balanco é formatado para float)
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

    #Um novo dicionário molde para criação ou edição de pedidos
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


# MENU
    pula_linha(5)
    w = input(space+ 'Balanço de caixa: ' + str(balanco) + '\n\n\n' + space+ 'CAIXA\n\n' + space+ '(E) Entradas\n' + space+ '(S) Saídas\n\n' + space+ 'GERENCIAMENTO DE PEDIDO\n\n' + space+ '(1) Criar pedido\n' + space+ '(2) Editar pedido\n' + space+ '(3) Consultar pedido\n' + space+ '(4) Consultar pedidos em andamento\n' + space+ '(5) Remover pedido\n' + space+ '(6) Concluir pedido\n\n' + space+ 'HISTÓRICOS\n\n' + space+ '(7) Pedidos\n'+ space+'(8) Entradas\n'+ space+ '(9) Saídas\n' + space+ '(0) Balanço\n\n' + space+ '(Q) Sair\n' + space+ '==>  ').upper()

# ENTRADAS
    if w == 'E':

        pula_linha(9)
        entrada = input(space + 'R$ ').replace(',', '.')
        balanco = balanco + float(entrada)
        
        #DOWNLOAD HIST. ENTRADAS
        downtxt('entrada.txt', entrada)

        #DOWNLOAD HIST. BALANÇO
        downtxt('balanco.txt', balanco)


# SAÍDAS
    elif w == 'S':

        pula_linha(9)
        saida = input(space + 'R$ ').replace(',', '.')
        balanco = balanco - float(saida)

        #DOWNLOAD HIST. SAÍDAS
        downtxt('saida.txt', saida)

        #DOWNLOAD HIST. BALANCO
        downtxt('balanco.txt', balanco)


# CRIAR PEDIDO
    elif w == '1':

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
            pedi['pecas'] = input(space +'Número de PEÇAS inválido, digite novamente usando somente números inteiros: ')
            check = pedi['pecas'].isdigit()
        
        pula_linha(9)
        print(space +'NUMERO do pedido: ' +pedi['numero'])

        print(space +'NOME do pedido: ' +pedi['nome'])
        print(space +'TELEFONE do pedido: ' +pedi['telefone'])

        print(space +'Número de PEÇAS: ' +pedi['pecas'])
        pedi['descricao'] = input(space +'DESCRIÇÃO do pedido: ') 

        pedi['entrega'] = input(space +'DATA DE ENTREGA do pedido: ')
        
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
        pedi['total'] = input(space + 'VALOR TOTAL do pedido: ')
        pedi['data'] = datetime.datetime.now().strftime('%d/%m/%y')
        
        pedidos[pedi['numero']] = pedi
        
        pula_linha(9)
        for k,v in pedi.items():
                    print(space, k +': ' +str(v))
        l = input('\n' + space + 'Pressione ENTER para salvar e voltar')
        down(pedidos, 'pedidos.json')


# EDITAR PEDIDO
    elif w == '2':

        pula_linha(10)
        w = input(space +'Digite o NUMERO do pedido que deseja editar \n' +space +' ==>  ')
        
        if w in pedidos:
            pedi = pedidos[w].copy()

        #MENU DE EDIÇÃO
            
            done = False
            while done == False:
                pula_linha(8)
                print(space +'MENU EDIÇÃO')
                print(space +'(salve as alterações antes de sair do menu edição)\n')
                pedi['nome'] = pedi['nome'].upper()
                for key, value in pedi.items():
                    print(space + key +':', pedi[key])
                print('\n' +space +'[S] salvar [Q] sair')
                b = input(space +'Digite o item a ser editado \n' +space +' ==>  ').lower()

                if b == 'numero':
                    pula_linha(10)
                    print(space +'Não é possível alterar o número do pedido, se necessário crie outro pedido\n')
                    b = input(space +'Pressione ENTER para continuar')
                
                #SAVE
                elif b == 's':
                    pedidos[w] = pedi
                    b = input(space +'Salvo!\n' +space +'Pressione ENTER para continuar')
                    down(pedidos, 'pedidos.json')

                #QUIT
                elif b == 'q':
                    pedi = dict()
                    done = True
                
                #ALTERA
                elif b != 'q' or b != 's':
                    pula_linha(10)
                    if b in pedi:
                        print(f'{space}{b}: {pedi[b]}\n')
                        pedi[b] = input(space +' ==>  ').replace(',', '.')

                    else:
                        print(space +'Não foi possível encontrar este item\n')
                        b = input(space +'Pressione ENTER para voltar ao menu edição')
        
        else:
            print(space +'Não foi possível localizar o pedido\n')
            w = input(space +'Pressione ENTER para voltar')

# LOCALIZAR PEDIDO
    elif w == '3':

        pula_linha(10)
        w = input(space +'NUMERO, NOME ou TELEFONE do pedido \n' + space + ' ==>  ').upper()
        pedi = dict()
        encon = False
        
        for nume, info in pedidos.items():
            if w == nume:
                pula_linha(9)
                for k in info:
                    print(space, k  +':', info[k])
                encon = True
            elif w == info['nome']:
                pula_linha(9)
                for k in info:
                    print(space, k +':', info[k])
                encon = True
            elif w == info['telefone']:
                pula_linha(9)
                for k in info:
                    print(space, k +':', info[k])
                encon = True 
        
        if encon == False:
            print(space +'Não foi possível encontrar esse pedido, consulte os pedidos em andamento se necessário')
        l = input('\n' + space + 'Pressione ENTER para voltar')


# PEDIDOS EM ANDAMENTO
    elif w == '4':

        pula_linha(0)
        print(space +'Numero | Nome | Telefone | Descrição')
        print(space +'________________________________________________')
        for key in pedidos:
            pedi = pedidos[key]
            print(space +pedi['numero'] +'   ' +pedi['nome'] +'   ' +pedi['telefone'] +'   ' +pedi['descricao'])
            print(space +'________________________________________________')
        l = input('\n' +space +'Pressione ENTER para voltar')


# REMOVER PEDIDO
    elif w == '5':

        pula_linha(10)
        w = input(space+'NUMERO do pedido que deseja remover \n' + space + ' ==>  ').upper()
        try:
            del pedidos[w]
            down(pedidos, 'pedidos.json')
        except:
            print(space +'Número invalido')
            l = input('\n' +space  +'Pressione ENTER para voltar')


# CONCLUSÃO DE PEDIDO
    elif w == '6':

        pula_linha(10)
        w = input(space +'NUMERO do pedido concluído \n' +space +' ==>  ').upper()
        try:
            historico[w] = pedidos[w]
            del pedidos[w]
            l = input('\n' +space  +'Pressione ENTER para voltar')
            down(historico, 'historico.json')
        except:
            print(space +'Número invalido')
            l = input('\n' +space  +'Pressione ENTER para voltar')


# EXIBIÇÃO DO HISTÓRICO
    elif w == '7':

        pula_linha(0)
        for key in historico:
            pedi = historico[key]
            print(pedi)
            print('\n')
        l = input('\n  Pressione ENTER para voltar')


# HISTORICO ENTRADAS
    elif w == '8':

        pula_linha(0)
        with open('entrada.txt', 'r') as file:
            for line in file:
                print(space + line)

        enter = input('\n' +space+ 'Pressione ENTER para voltar')


#HISTORICO SAIDAS
    elif w == '9':

        pula_linha(0)
        with open('saida.txt', 'r') as file:
            for line in file:
                print(space + line)
        
        enter = input('\n' +space+ 'Pressione ENTER para voltar')

#HISTORICO BALANÇO
    elif w == '0':

        pula_linha(0)
        with open('balanco.txt', 'r') as file:
            for line in file:
                print(space + line)

        enter = input('\n' +space+ 'Pressione ENTER para voltar')


# FECHAR PROGRAMA
    elif w == 'Q':

        down(historico, 'historico.json')
        down(pedidos, 'pedidos.json')
        break