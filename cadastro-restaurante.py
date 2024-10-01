import json
import os

print("RESTAURANTE MANAGER")

ARQUIVO_RESTAURANTES = 'dados_dos_restaurantes.txt'
restaurantes = {}

def carregar_restaurantes():
    global restaurantes
    if os.path.exists(ARQUIVO_RESTAURANTES):
        with open(ARQUIVO_RESTAURANTES, 'r') as f:
            restaurantes = json.load(f)

def salvar_restaurantes():
    with open(ARQUIVO_RESTAURANTES, 'w') as f:
        json.dump(restaurantes, f)

def cadastrar_restaurante(nome):
    if nome in restaurantes:
        print("Restaurante já existe.")
    else:
        pratos = {}
        while True:
            prato = input("Digite o nome do prato (ou 'sair' para terminar): ")
            if prato.lower() == 'sair':
                break
            preco = float(input(f"Digite o preço do prato '{prato}': R$"))
            pratos[prato] = preco
        restaurantes[nome] = pratos
        salvar_restaurantes()
        print(f"Restaurante '{nome}' cadastrado com sucesso!")

def listar_pratos(nome_restaurante):
    if nome_restaurante in restaurantes:
        print(f"Pratos do restaurante {nome_restaurante}:")
        for prato, preco in restaurantes[nome_restaurante].items():
            print(f"{prato}: R${preco:.2f}")

        total = 0
        while True:
            pedido = input("Digite o nome do prato que deseja pedir (ou 'sair' para finalizar o pedido): ")
            if pedido.lower() == 'sair':
                break
            if pedido in restaurantes[nome_restaurante]:
                total += restaurantes[nome_restaurante][pedido]
                print(f"Adicionado {pedido}: R${restaurantes[nome_restaurante][pedido]:.2f}. Total até agora: R${total:.2f}")
            else:
                print("Prato não encontrado no menu.")
        
        print(f"Total do seu pedido: R${total:.2f}")
        pagamento = input(f"O pagamento sera no dinhero, cartão ou pix? ")
        if pagamento == "dinheiro":
            print("ok pagamento com o entregador! :)")
            print("obrigado, volte sempre!!!")

        elif pagamento == "cartão":
            print("ok, o entregador levara a maquininha para o pagamento! :)")
            print("obrigado, volte sempre!!!")

        elif pagamento == "pix":
            print("ok, pague com o qrcod no nosso perfil! :)")
            print("obrigado, volte sempre!!!")

    else:
        print("Restaurante não encontrado.")

def listar_restaurantes():
    if restaurantes:
        print("Restaurantes cadastrados:")
        for nome in restaurantes.keys():
            print(f"- {nome}")
    else:
        print("Nenhum restaurante cadastrado.")

def main():
    carregar_restaurantes()

    while True:
        print("\n1. Cadastrar Restaurante")
        print("2. Fazer Pedido")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do restaurante: ")
            cadastrar_restaurante(nome)
            

        elif opcao == '2':
            listar_restaurantes()
            nome_restaurante = input("Digite o nome do restaurante para listar os pratos: ")
            listar_pratos(nome_restaurante)
            break

        elif opcao == '3':
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")


main()
