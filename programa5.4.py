import json
from pprint import pprint

with open('estoque.json', 'r') as arquivo:
    dicionario = json.loads(arquivo.read())



loja = input("Digite o nome da loja ")
print("0 - sair\n1 - adicionar item\n2 - remover item\n3 - alterar item\n4 - imprimir estoque\n5 - listar estoques faltando\n6 - imprimir valor total do estoque")

def lojas(loja):

    def options():
        op = int(input("Escolha uma opção(0-6) "))
        return op

    def modificacoes_estoque(escolha):
        if escolha == 1:
            if loja not in estoque:
                produto = input("Digite o nome do produto que deseja ADICIONAR ")
                valor = int(input('Digite a QUANTIDADE do produto '))
                preco = float(input('Digite o preço unitário do produto '))
                if preco > 0:
                    adicionar = estoque.update({loja: {produto: {'Quantidade': valor, 'Preço': preco}}})
                    print('Produto adicionado!')
                return estoque
            if loja in estoque:
                produto = input("Digite o nome do produto que deseja ADICIONAR ")
                valor = int(input('Digite a QUANTIDADE do produto '))
                preco = float(input('Digite o preço unitário para o produto '))
                if preco > 0:
                    adicionar = estoque[loja].update( {produto: {'Quantidade': valor, 'Preço': preco}})
                    print('Produto adicionado!')

        elif escolha == 2:
            produto = input("Digite o nome do produto que deseja REMOVER ")
            del estoque[loja][produto]
            print('Produto deletado!')
            return estoque

        elif escolha == 3:
            mod = int(input("Digite o que você deseja modificar (VALOR[1] PREÇO[2]) "))
            if mod == 1:
                produto = input("Digite o nome do produto que deseja MODIFICAR ")
                valor = int(input('Digite um NOVO valor '))
                estoque[loja][produto]['Quantidade'] = valor
                print('Valor alterado!')
                return estoque
            elif mod == 2:
                produto = input("Digite o nome do produto que deseja MODIFICAR ")
                preco = float(input("Digite o NOVO preço do produto "))
                estoque[loja][produto]['Preço'] = preco
                print('Preço alterado! ')
            return estoque

        elif escolha == 4:
            for k,v in estoque[loja].items():
                print('Produto:{0}\n\tQuantidade:{1} produtos\n\tPreço unitário:R${2}' .format(k, v['Quantidade'], v['Preço']))
            return estoque

        elif escolha == 5:
            for k,v in estoque[loja].items():
                b = v['Quantidade']
                if b < 0:
                    estoque_faltando.append(k)
            for e in range(0, len(estoque_faltando)):
                print(estoque_faltando[e])
            return estoque

        elif escolha == 6:
            for valor in estoque[loja].values():
                if valor["Quantidade"] > 0:
                    v = valor["Quantidade"] * valor["Preço"]
                    lista_multiplicacao.append(v)
                    total = sum(lista_multiplicacao)
            print('R${0}'.format(total))
            return total

    lista_multiplicacao = []
    escolha = options()
    estoque = dicionario
    estoque_faltando = []

    while escolha != 0:
        modificacoes_estoque(escolha)
        print("0 - sair\n1 - adicionar item\n2 - remover item\n3 - alterar item\n4 - imprimir estoque\n5 - listar estoques faltando\n6 - imprimir valor total do estoque")
        escolha = options()
        if escolha == 6:
            print('O valor total do estoque é de R${0}'.format(total))

    if escolha == 0:
        print('Até mais! ')

    estoque_json = json.dumps(estoque, sort_keys=True, indent=4)
    with open('estoque.json', 'w') as arquivo:
        arquivo.write(estoque_json)

lojas(loja)