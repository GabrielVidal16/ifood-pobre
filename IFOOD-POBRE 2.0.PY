import json
import os

nome = ""

print("IFOOD POBRE")

ARQUIVO_USUARIOS = 'dados_do_usuarios.txt'
usuarios = {}

def carregar_usuarios():
    global usuarios
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, 'r') as f:
            usuarios = json.load(f)  

def salvar_usuarios():
    with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, ensure_ascii=False) 


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
        pass
    else:
        print("Nome de usuário ou senha incorretos, tente novamente: ")
        nome = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")
        fazer_login(nome,senha)

    os.system('cls')

def verificar_usuario(nome):
    if nome in usuarios:
        print(f"\nBem-vindo de volta, {nome}!")
    input("")

def nova_tela(mensagem) :
    
    os.system('cls')
    print(mensagem + "\n")

def menu_usuarios():
    carregar_usuarios() 
    os.system('cls') 
    while True:
        
        nova_tela("IFOOD POBRE")
        print("1. Cadastrar Usuário")
        print("2. Fazer Login")
        print("3. Sair")
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '1':
            nova_tela("CADASTRO DE USUARIOS")

            nome = input("Digite o nome de usuário: ").lower()

            if nome == "" or nome.isdigit() or len(nome) < 3 :
                if nome == "" :
                    input("Você precisa preencher este campo")
                elif nome.isdigit():
                    input("Digite seu nome sem numeros")
                if len(nome) < 3 :
                    input("Você digitou um nome muito curto")
                continue
            
            senha = input("Digite a senha: ")
            if senha == "" or len(senha) < 3 :
                if senha == "" :
                    input("Você precisa preencher este campo")
                else:
                    if len(senha) < 3 :
                        input("Sua senha nao pode ser tao curta")
                continue
            
            endereco = input("Digite o nome da sua rua: ")
            if endereco == "" or endereco.isdigit() or len(endereco) < 6 :
                if endereco == "" :
                    input("Você precisa preencher este campo")
                elif endereco.isdigit():
                    input("Digite seu endereço sem numeros")
                if len(endereco) < 8 :
                    input("Você digitou um endereço invalido")
                continue

            input(f"Bem-vindo {nome}!")
             
            cadastrar_usuario(nome, senha, endereco)
            break

        elif opcao == '2':
            nova_tela("LOGIN")
            nome = input("Digite o nome de usuário: ").lower()
            senha = input("\nDigite a senha: ")
            fazer_login(nome, senha)
            verificar_usuario(nome)
            break

        elif opcao == '3':
            nova_tela("Saindo do sitema")
            exit()
        
        else:
            print("Opção inválida. Tente novamente.")
    
if __name__ == '__main__' :
    menu_usuarios()

# funçoes dos restaurantes 

ARQUIVO_RESTAURANTES = 'dados_dos_restaurantes.txt'
restaurantes = {}

def carregar_restaurantes():
    global restaurantes
    if os.path.exists(ARQUIVO_RESTAURANTES):
        with open(ARQUIVO_RESTAURANTES, 'r') as f:
            restaurantes = json.load(f)


with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as f:
            json.dump(usuarios, f, ensure_ascii=False)

def salvar_restaurantes():
    with open(ARQUIVO_RESTAURANTES,'w', encoding="utf-8") as f:
        json.dump(restaurantes, f, ensure_ascii=False)

def cadastrar_restaurante(nome):
    if nome in restaurantes:
        print("Restaurante já existe.")
    else:
        pratos = {}
        while True:
            prato = input("\nDigite o nome do prato (ou 'sair' para terminar): ")
            if prato.lower() == 'sair':
                break

            elif prato == "" :
                print("É necessario pelo menos um prato para seu restaurante")
                pass

            elif prato.isdigit() :
                print("O nome do seu prato nao pode ser um numero")
                pass
            
                
            elif prato != "" :

                try :
                    preco = float(input(f"\nDigite o preço do prato '{prato}': R$"))

                except:
                    print("\nO prato nao pode custar 0 reais\n")
                    continue

                if isinstance(preco, float) :
                    if preco <= 0 :
                        print("Seu prato nao pode custar 0 Reais")
                    else :
                        pratos[prato] = preco
                        restaurantes[nome] = pratos
                        salvar_restaurantes()
                        print(f"Restaurante '{nome}' cadastrado com sucesso!")
                else: print("digita certo animal")

            else : 
                print("Insira apenas numeros")
        
        

def listar_pratos(nome_restaurante):
    if nome_restaurante in restaurantes:
        os.system('cls')
        print(f"""{nome_restaurante.upper()}
≡≡≡≡≡≡≡≡≡≡≡≡""")
        print(f"""\nPratos do Restaurante:
""")


        for prato, preco in restaurantes[nome_restaurante].items():
            print(f"""{prato}: R${preco:.2f}\n⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺""")

        total = 0
        lista_pedidos = []
        while True:
            pedido = input("\nDigite o nome do prato que deseja pedir ('finalizar' para finalizar o pedido, ou 'sair para voltar ao menu): ")

            if pedido.lower() == 'finalizar':
                break

            elif pedido.lower() == 'sair' and lista_pedidos == [] :
                menu_restaurantes()

            elif pedido.lower() == 'sair' and lista_pedidos != [] :
                
                escolha = input("\nVocê tem certeza que deseja sair? você possui itens em seu carrinho: ")
                if escolha == 'sim' or escolha == 's' :
                    menu_restaurantes()

            if pedido.lower() in restaurantes[nome_restaurante]:

                lista_pedidos.append(pedido)
                total += restaurantes[nome_restaurante][pedido]
                print(f"\nAdicionado {pedido}: R${restaurantes[nome_restaurante][pedido]:.2f}. Total até agora: R${total:.2f}")
                
            else:
                print("Prato não encontrado no menu.")
        
        if lista_pedidos == [] and total == 0 :
            input("\nvoce nao adicionou nada ao carrinho")
            listar_pratos(nome_restaurante)

        elif lista_pedidos != [] and total > 0:
            print(f"\nseu pedido ficou:{lista_pedidos}\n")
            print(f"\nTotal do seu pedido: R${total:.2f}")

            salvar_pedido(nome_restaurante,lista_pedidos,total)
        
            pagamento = input(f"O pagamento sera no dinheiro, cartão ou pix? ")
            print("\n")
            if pagamento == "dinheiro":
                print("ok pagamento com o entregador! :)")
                print("obrigado, volte sempre!!!")
                exit()

            elif pagamento == "cartão":
                print("ok, o entregador levara a maquininha para o pagamento! :)")
                print("obrigado, volte sempre!!!")
                exit()

            elif pagamento == "pix":
                print("ok, pague com o qr code no nosso perfil! :)")
                print("obrigado, volte sempre!!!")
                exit()

    else :
        print("\nRestaurante não encontrado\n")
        nome_restaurante = input("Tente novamente: ")
        listar_pratos(nome_restaurante)

     

def listar_restaurantes():
  
    nova_tela("RESTAURANTES CADASTRADOS")
    dicionario_restaurantes = {}
    
    for indice, nome in enumerate(restaurantes.keys(), start=1):
        print(f"({indice}) - {nome}")
        dicionario_restaurantes[indice] = nome

    return dicionario_restaurantes

def menu_restaurantes():
    carregar_restaurantes()

    while True:
        
        nova_tela("IFOOD POBRE")
        print("1. Cadastrar Restaurante")
        print("2. Fazer Pedido")
        print("3. Sair")
        opcao = input("\nEscolha uma opção: ")

        match opcao:

            case '1' :
                nova_tela("CADASTRO DE RESTAURANTE")
                nome = input("Digite o nome do restaurante: ")

                cadastrar_restaurante(nome)

            case '2' :

                dicionario_restaurantes = listar_restaurantes()

                try:
                    nome_restaurante = int(input("\nDigite o número do restaurante para listar os pratos, ou '0' para voltar: "))
                    
                    if nome_restaurante in dicionario_restaurantes:
                        listar_pratos(dicionario_restaurantes[nome_restaurante])
                    elif nome_restaurante == 0:
                        continue
                    
                    else:
                        input("\nNúmero inválido.")

                except ValueError:
                    input("\nPor favor, insira um número válido.")

                          
            case '3':
                print("Saindo do sistema.")
                break

            case _ :
                print("Opção inválida. Tente novamente.")


def salvar_pedido(nome_restaurante, lista_pedidos, total):
    nome_arquivo = 'pedidos.txt' 
    with open(nome_arquivo, 'a', encoding='utf-8') as f:
        f.write(f"Pedido do Restaurante: {nome_restaurante}\n")
        f.write("Pratos pedidos:\n")
        for prato in lista_pedidos:
            f.write(f"- {prato}\n")
        f.write(f"\nTotal do pedido: R${total:.2f}\n")
        f.write("="*30 + "\n")

menu_restaurantes()