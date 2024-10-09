tarefa = []

def adicionar_tarefa():
    a = input("digite uma terefa: ")
    tarefa.append(a)
    return a
def retirar_tarefa():
    print(tarefa)
    a = input("digite a tarefa que deseja retirar:  ")
    
    tarefa.remove(a)
    print("sua tarefa foi retirada",tarefa)
            

def resultado_final():
    print(tarefa)