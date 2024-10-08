import json
import os 

ARQUIVO_PEDIDOS = 'pedidos.txt'
pedidos = {}

def carregar_pedidos():
    global pedidos
    if os.path.exists(ARQUIVO_PEDIDOS):
        with open(ARQUIVO_PEDIDOS, 'r') as f:
            pedidos = json.load(f)  

def salvar_pedidos():
    with open(ARQUIVO_PEDIDOS, 'w',encoding="UTF-8") as f:
        json.dump(pedidos, f, ensure_ascii=False)  

def cadastrar_pedidos(nome, prato, endereco):
    if nome in pedidos:
        print("Usuário já existe.")
    else:
        pedidos[nome] = {
            'prato': prato,
            'endereco': endereco
        }
        salvar_pedidos()  

ARQUIVO_PEDIDOS.append(lista_pedidos)

def main():
    carregar_pedidos()

    while True:
        print("\n1. Cadastrar Restaurante")
        print("2. Fazer Pedido")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do restaurante: ")
            cadastrar_pedidos(nome)
            

        elif opcao == '2':
            salvar_pedidos()
            nome_restaurante =("")
            (nome_restaurante)
            break

        elif opcao == '3':
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")


main()



    

