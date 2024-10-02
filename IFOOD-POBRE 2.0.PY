import json
import os

print("IFOOD-POBRE")

ARQUIVO_USUARIOS = 'dados_do_usuarios.txt'
usuarios = {}

def carregar_usuarios():
    global usuarios
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, 'r') as f:
            usuarios = json.load(f)  

def salvar_usuarios():
    with open(ARQUIVO_USUARIOS, 'w') as f:
        json.dump(usuarios, f)  

def cadastrar_usuario(nome, senha, endereco):
    if nome in usuarios:
        print("Usuário já existe.")
    else:
        usuarios[nome] = {
            'senha': senha,
            'endereco': endereco
        }
        salvar_usuarios()  
        print("Usuário cadastrado com sucesso!")

def fazer_login(nome, senha):
    if nome in usuarios and usuarios[nome]['senha'] == senha:
        print(f"Bem-vindo, {nome}!")
    else:
        print("Nome de usuário ou senha incorretos.")

def verificar_usuario(nome):
    if nome in usuarios:
        print(f"Bem-vindo de volta, {nome}!")

def menu_usuarios():
    carregar_usuarios()  

    while True:
        print("\n1. Cadastrar Usuário")
        print("2. Fazer Login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")
            endereco = input("Digite seu endereço: ")
            verificar_usuario(nome)  
            cadastrar_usuario(nome, senha, endereco)
            break
        elif opcao == '2':
            nome = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")
            fazer_login(nome, senha)
            break
        elif opcao == '3':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_usuarios()



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
        print(f"seu pedido ficou:{pedido}")
        print(f"Total do seu pedido: R${total:.2f}")

        if total ==0:
            print("voce nao adicionou nada ao carrinho")
            listar_pratos(nome_restaurante)

        if total >0:
        
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

def menu_restaurantes():
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


menu_restaurantes()
