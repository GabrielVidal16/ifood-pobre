import json
import os

ARQUIVO_RESTAURANTES = 'restaurantes.txt'
restaurantes = {}

def carregar_RESTAURANTES():
    
    global restaurantes
    if os.path.exists(ARQUIVO_RESTAURANTES):
        with open(ARQUIVO_RESTAURANTES, 'r') as f:
            linhas= f.readlines()

            if len(linhas) > 0:
                restaurantes = json.load(f)

def salvar_RESTAURANTES():
    
    with open(ARQUIVO_RESTAURANTES, 'a') as f:
        json.dump(restaurantes, f)

def cadastrar_RESTAURANTES(nome, prato, proco):
    if nome in restaurantes:
        print("restaurante já existe.")
    else:
        restaurantes[nome] = {
            'prato': prato,
            'preco': proco
        }
        salvar_RESTAURANTES()  
        print("restaurante cadastrado com sucesso!")

  

def verificar_RESTAURANTES(nome):
    print('restaurantes.txt')
    

def main():
    carregar_RESTAURANTES()  

    while True:
        print("\n1. Cadastrar restaurante")
        print("2. ver restaurantes")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do restaurante: ")
            prato = input("Digite seus pratos: ")
            preco = input("Digite os preços de cada prato: ")
            verificar_RESTAURANTES(nome)  
            cadastrar_RESTAURANTES(nome, prato, preco)
            break
        elif opcao == '2':
            verificar_RESTAURANTES()
        elif opcao == '3':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
