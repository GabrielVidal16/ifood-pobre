import json
import os

print("IFOOD-POBRE")

ARQUIVO_USUARIOS = 'usuarios.txt'


usuarios = {}

def carregar_usuarios():
    
    global usuarios
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, 'r') as f:
            linhas= f.readlines()

            if len(linhas) > 0:
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
    

def main():
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
    main()
