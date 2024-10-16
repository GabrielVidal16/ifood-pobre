import os
import json
joao = {"nome":"joao","idade":15}
maria = {"nome":"maria","idade":20}
pedro = {"nome":"pedro","idade":27}

ARQUIVO_USUARIOS = "usuarios_dicionario.txt"

usuario = {}

def salvar_usuario(path_file, dicionario:dict):
    if os.path.exists(path_file):
        with open(path_file, 'a',encoding="utf-8") as f:

            for i, (chave, valor) in enumerate(dicionario.items()):
                if i == len(dicionario) - 1:
                    f.write(f' / Último item: {chave}: {valor}\n')
                else:
                    f.write(f'Item: {chave}: {valor}')
    else:    
        with open(path_file, 'w',encoding="utf-8") as f:
            for i, (chave, valor) in enumerate(dicionario.items()):
                if i == len(dicionario) - 1:
                    f.write(f' / Último item: {chave}: {valor}\n')
                else:
                    f.write(f'Item: {chave}: {valor}')

salvar_usuario("usuarios.txt",joao)

salvar_usuario("usuarios.txt",maria)

salvar_usuario("usuarios.txt",pedro)


