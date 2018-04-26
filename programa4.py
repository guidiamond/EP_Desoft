import json
from pprint import pprint

with open('estoque.json', 'r') as arquivo:
    dicionario = json.loads(arquivo.read())


def options():
    opcoes = print("0 - sair\n1 - adicionar item\n2 - remover item\n3 - alterar item\n4 - imprimir estoque\n5 - listar estoques faltando\n6 - imprimir valor total do estoque")
    op = int(input("Escolha uma opção(0-6) "))
    return op


def modificacoes_estoque(escolha):
    if escolha == 1:
        produto = input("Digite o nome do produto que deseja ADICIONAR ")
        valor = int(input('Digite um valor '))
        preco = float(input('Digite o preço unitário para o produto '))
        if preco > 0:
            adicionar = estoque.update({produto: {'Quantidade': valor, 'Preço': preco}})

        return estoque

    elif escolha == 2:
        produto = input("Digite o nome do produto que deseja REMOVER ")
        del estoque[produto]
        return estoque

    elif escolha == 3:
        mod = int(input("Digite o que você deseja modificar (VALOR[1] PREÇO[2]) "))
        if mod == 1:
            produto = input("Digite o nome do produto que deseja MODIFICAR ")
            valor = int(input('Digite um NOVO valor '))
            estoque[produto]['Quantidade'] = valor
            return estoque
        elif mod == 2:
            produto = input("Digite o nome do produto que deseja MODIFICAR ")
            preco = float(input("Digite o NOVO preço do produto "))
            estoque[produto]['Preço'] = preco
        return estoque
    elif escolha == 4:
        print(estoque)
        return estoque

    elif escolha == 5:
        for k,v in estoque.items():
            a = k
            b = v['Quantidade']
            if b < 0:
                estoque_faltando.append(a)
                print(estoque_faltando)
    elif escolha == 6:
        for valor in estoque.values():
            if valor["Quantidade"] > 0:
                v = valor["Quantidade"] * valor["Preço"]
                lista_multiplicacao.append(v)
                total = sum(lista_multiplicacao)
                """"
                
                
                
                
                
                
                
                
                
                """

        print('R${0}'.format(total))
        return total
lista_multiplicacao = []
escolha = options()
estoque = dicionario
estoque_faltando = []

while escolha != 0:
    modificacoes_estoque(escolha)
    escolha = options()

estoque_json = json.dumps(estoque, sort_keys=True, indent=4)
with open('estoque.json', 'w') as arquivo:
    arquivo.write(estoque_json)