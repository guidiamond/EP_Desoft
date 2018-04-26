def options():
    opcoes = print("0 - sair\n1 - adicionar item\n2 - remover item\n3 - alterar item\n4 - imprimir estoque")
    op = int(input("Escolha uma opção(0-4) "))

    return op

def modificacoes(escolha):
    if escolha == 1:
        produto = input("Digite o nome do produto que deseja ADICIONAR ")
        valor = int(input('Digite um valor '))
        estoque.update({produto:{'Quantidade':valor}})
        return estoque

    elif escolha == 2:
        produto = input("Digite o nome do produto que deseja REMOVER ")
        del estoque[produto]

    elif escolha == 3:
        produto = input("Digite o nome do produto que deseja MODIFICAR ")
        valor = int(input('Digite um NOVO valor '))
        estoque[produto]['quantidade'] = valor

    elif escolha == 4:
        print(estoque)

escolha = options()

estoque = {}

while escolha != 0:
    modificacoes(escolha)
    escolha = options()

print(estoque)