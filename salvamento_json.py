import json
import os


ARQUIVO_USUARIOS = 'usuarios_json.txt'
usuarios = {}


def salvar_usuarios():
    with open(ARQUIVO_USUARIOS, "a", encoding="utf-8") as f:
        json.dump(usuarios, f, ensure_ascii=False) 


def cadastrar_usuario(nome, idade ):
     if nome in usuarios:
         print("Usuário já existe.")
     else:
        usuarios[nome] = {
            'idade': idade
         }
        salvar_usuarios()  


def menu():
    
    while True:
        
        
        print("\n1. Cadastrar Usuário")
        
        print("2. Sair")
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '1':

            nome = input("\nDigite o nome de usuário: ").lower()

            if nome in usuarios:
                print("\nesse nome ja existe...")
                print("escolha outro nome")
                menu()

            elif nome == "" :
                    input("\nVocê precisa preencher este campo")
            elif nome.isdigit():
                    input("\nDigite seu nome sem numeros")
            
            idade = int(input("\nDigite sua idade: "))
            
            if idade == "" :
                input("\nVocê precisa preencher este campo")
        
        
        elif opcao == "2":
            print("\nsaindooooo")
            break
        
        elif opcao != 1 and opcao != 2:
            print("\nvoce nao escolheu nenhuma opçao")
            return menu()

        
        cadastrar_usuario(nome, idade)
        menu_final()
        break

def menu_final():
    while True:
        opcao_final = int(input("\n1- continuar salvando 2-sair: "))
        
        if opcao_final == 1:
            menu()
        elif opcao_final == 2:
            print("\nsaindooo")
            break
        elif opcao_final != 1 and opcao_final != 2:
            print("\nvoce nao escolheu nenhuma opçao")
            return menu()
    

menu()
print(usuarios)  
       