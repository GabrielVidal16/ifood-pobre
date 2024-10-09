import json
import os

# ... (restante do seu código)

def salvar_pedido(nome_restaurante, lista_pedidos, total):
    nome_arquivo = f'pedido_{nome_restaurante}.txt'
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write(f"Pedido do Restaurante: {nome_restaurante}\n")
        f.write("Pratos pedidos:\n")
        for prato in lista_pedidos:
            f.write(f"- {prato}\n")
        f.write(f"\nTotal do pedido: R${total:.2f}\n")
    print(f"\nSeu pedido foi salvo em {nome_arquivo}")

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
            pedido = input("\nDigite o nome do prato que deseja pedir ('finalizar' para finalizar o pedido, ou 'sair' para voltar ao menu): ")
            if pedido.lower() == 'finalizar':
                break

            elif pedido.lower() == 'sair':
                menu_restaurantes()

            if pedido.lower() in restaurantes[nome_restaurante]:
                lista_pedidos.append(pedido)
                total += restaurantes[nome_restaurante][pedido]
                print(f"\nAdicionado {pedido}: R${restaurantes[nome_restaurante][pedido]:.2f}. Total até agora: R${total:.2f}")
            else:
                print("Prato não encontrado no menu.")
        
        if lista_pedidos == [] and total == 0:
            input("\nVocê não adicionou nada ao carrinho.")
            listar_pratos(nome_restaurante)

        elif lista_pedidos != [] and total > 0:
            print(f"\nSeu pedido ficou: {lista_pedidos}\n")
            print(f"\nTotal do seu pedido: R${total:.2f}")
            
            salvar_pedido(nome_restaurante, lista_pedidos, total)  # Salvar pedido

            pagamento = input(f"O pagamento será em dinheiro, cartão ou pix? ")
            print("\n")
            if pagamento == "dinheiro":
                print("Ok, pagamento com o entregador! :)")
                print("Obrigado, volte sempre!!!")

            elif pagamento == "cartão":
                print("Ok, o entregador levará a maquininha para o pagamento! :)")
                print("Obrigado, volte sempre!!!")

            elif pagamento == "pix":
                print("Ok, pague com o QR code no nosso perfil! :)")
                print("Obrigado, volte sempre!!!")

    else:
        print("\nRestaurante não encontrado\n")
        nome_restaurante = input("Tente novamente: ")
        listar_pratos(nome_restaurante)

# ... (restante do seu código)
