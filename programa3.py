import json
from pprint import pprint

with open('estoque.json', 'r') as arquivo:
    dicionario = json.loads(arquivo.read())

def options():
    opcoes = print("0 - sair\n1 - adicionar item\n2 - remover item\n3 - alterar item\n4 - imprimir estoque")
    op = int(input("Escolha uma opção(0-4) "))

    return op

def modificacoes_estoque(escolha):
    if escolha == 1:
        produto = input("Digite o nome do produto que deseja ADICIONAR ")
        valor = int(input('Digite um valor '))
        estoque.update({produto:{'Quantidade':valor}})
        return estoque

    elif escolha == 2:
        produto = input("Digite o nome do produto que deseja REMOVER ")
        del estoque[produto]
        return estoque

    elif escolha == 3:
        produto = input("Digite o nome do produto que deseja MODIFICAR ")
        valor = int(input('Digite um NOVO valor '))
        estoque[produto]['Quantidade'] = valor
        return estoque

    elif escolha == 4:
        print(estoque)
        return estoque

escolha = options()
estoque = dicionario

while escolha != 0:
    modificacoes_estoque(escolha)
    escolha = options()

print(estoque)

estoque_json = json.dumps(estoque, sort_keys=True, indent=4)
with open('estoque.json', 'w') as arquivo:
    arquivo.write(estoque_json)