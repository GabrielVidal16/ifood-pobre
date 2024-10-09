from operacoes import adicionar_tarefa,retirar_tarefa,resultado_final
from interface import exibir_menu, obter_opcao

def main():
    while True:
        exibir_menu()
        opcao = obter_opcao()

        if opcao == 4:
            print("Saindo...")
            break

        
        if opcao == 1:
            print(f"Resultado: {adicionar_tarefa()}")
        elif opcao == 2:
            print(f"Resultado: {retirar_tarefa()}")
        elif opcao == 3:
            print(f"Resultado: {resultado_final}")
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
