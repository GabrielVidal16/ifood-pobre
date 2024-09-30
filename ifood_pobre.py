import os

def salvar_variaveis(arquivo, **kwargs):
    with open(arquivo, 'a') as f:
        for nome, valor in kwargs.items():
            f.write(f"{nome}: {valor}\n")

def carregar_variaveis(arquivo):
    variaveis = {}
    with open(arquivo, 'r') as f:
        for line in f:
            nome, valor = line.strip().split(': ')
            variaveis[nome] = valor
    return variaveis

def registrar_usuario():
    nome = input("Digite seu nome: ")
    senha = input("Crie sua senha: ")  

    salvar_variaveis('dados_do_usuario.txt', nome=nome, senha=senha)
    print("Usuário registrado com sucesso!")


def verificar_usuario():
    
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ") 

    if os.path.exists("dados_do_usuario.txt"):
        variaveis = carregar_variaveis('dados_do_usuario.txt')
        
        
        if variaveis.get("nome") == nome and variaveis.get("senha") == senha:
            print("Seja bem-vindo novamente,", nome)
        elif variaveis.get("nome") == nome:
            print("Senha incorreta...")
        else:
            print("Usuário não encontrado.")
    else:
        print("Não há dados de usuários salvos.")

def main():
    while True:
        opcao = input("Escolha uma opção: 1 - Registrar, 2 - entrar, 3 - Sair: ")
        if opcao == '1':
            registrar_usuario()
            break
        elif opcao == '2':
            verificar_usuario()
            break
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()






