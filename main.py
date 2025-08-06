#Exibi todas as tarefas da lista
def mostrar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("Tarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")

#Adiciona uma nova tarefa à lista.
def adicionar_tarefa(tarefas):
    tarefa = input("Digite a descrição da nova tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada.")

#Atualiza uma tarefa existente na lista.
def atualizar_tarefa(tarefas):
    mostrar_tarefas(tarefas)
    if tarefas:
        try:
            indice = int(input("Número da tarefa que deseja atualizar: "))
            if 1 <= indice <= len(tarefas):
                nova_desc = input("Nova descrição: ")
                tarefas[indice - 1] = nova_desc
                print("Tarefa atualizada.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida.")

#Remove uma tarefa da lista.
def remover_tarefa(tarefas):
    mostrar_tarefas(tarefas)
    if tarefas:
        try:
            indice = int(input("Número da tarefa que deseja remover: "))
            if 1 <= indice <= len(tarefas):
                tarefas.pop(indice - 1)
                print("Tarefa removida.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida.")

#Função principal que exibe o menu e gerencia a execução do programa.
def main():
    tarefas = []
    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Mostrar tarefas")
        print("2. Adicionar tarefa")
        print("3. Atualizar tarefa")
        print("4. Remover tarefa")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            mostrar_tarefas(tarefas)
        elif escolha == '2':
            adicionar_tarefa(tarefas)
        elif escolha == '3':
            atualizar_tarefa(tarefas)
        elif escolha == '4':
            remover_tarefa(tarefas)
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

#Garante que o script será executado somente se for rodado diretamente
if __name__ == "__main__":
    main()
