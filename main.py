#Exibe todas as tarefas com descrição e status.
def mostrar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("Tarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa['descricao']} [{tarefa['status']}]")


#Adiciona uma nova tarefa com status 'pendente'.
def adicionar_tarefa(tarefas):
    descricao = input("Digite a descrição da nova tarefa: ")
    tarefas.append({"descricao": descricao, "status": "pendente"})
    print("Tarefa adicionada com status 'pendente'.")


#Atualiza a descrição de uma tarefa existente.
def atualizar_tarefa(tarefas):
    mostrar_tarefas(tarefas)
    if tarefas:
        try:
            indice = int(input("Número da tarefa que deseja atualizar: "))
            if 1 <= indice <= len(tarefas):
                nova_desc = input("Nova descrição: ")
                tarefas[indice - 1]["descricao"] = nova_desc
                print("Tarefa atualizada.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida.")


#Atualiza o status de uma tarefa existente.
def atualizar_status_tarefa(tarefas):
    mostrar_tarefas(tarefas)
    if tarefas:
        try:
            indice = int(
                input("Número da tarefa que deseja alterar o status: "))
            if 1 <= indice <= len(tarefas):
                novo_status = input(
                    "Novo status (pendente, em andamento, concluída): ").strip().lower()
                if novo_status in ["pendente", "em andamento", "concluída"]:
                    tarefas[indice - 1]["status"] = novo_status
                    print("Status atualizado.")
                else:
                    print("Status inválido.")
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


#Exibe apenas as tarefas com o status informado.
def filtrar_tarefas_por_status(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    status_filtro = input(
        "Digite o status para filtrar (pendente, em andamento, concluída): ").strip().lower()
    filtradas = [t for t in tarefas if t["status"] == status_filtro]

    if not filtradas:
        print(f"Nenhuma tarefa com status '{status_filtro}'.")
    else:
        print(f"Tarefas com status '{status_filtro}':")
        for i, tarefa in enumerate(filtradas, 1):
            print(f"{i}. {tarefa['descricao']}")


#Menu principal do sistema.
def main():
    tarefas = []

    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Mostrar tarefas")
        print("2. Adicionar tarefa")
        print("3. Atualizar descrição de tarefa")
        print("4. Remover tarefa")
        print("5. Atualizar status da tarefa")
        print("6. Filtrar tarefas por status")
        print("7. Sair")
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
            atualizar_status_tarefa(tarefas)
        elif escolha == '6':
            filtrar_tarefas_por_status(tarefas)
        elif escolha == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
