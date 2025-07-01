import json  # Importa módulo para salvar/carregar arquivos JSON

# Função para salvar a lista de tarefas em um arquivo JSON
def salvar_tarefas(tarefas, nome_arquivo="tarefas.json"):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=4)

# Função para carregar a lista de tarefas de um arquivo JSON
def carregar_tarefas(nome_arquivo="tarefas.json"):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        # Retorna lista vazia se o arquivo ainda não existir
        return []

# Função para adicionar uma nova tarefa
def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa.strip(), "completada": False}
    tarefas.append(tarefa)
    return f"Tarefa '{nome_tarefa}' foi adicionada com sucesso!"

# Função para exibir todas as tarefas na tela
def ver_tarefas(tarefas):
    print("\nLista de Tarefas:")
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else " "
        print(f"{indice}. [{status}] {tarefa['tarefa']}")

# Função para atualizar o nome de uma tarefa específica
def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    try:
        indice = int(indice_tarefa) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["tarefa"] = novo_nome_tarefa.strip()
            return f"Tarefa {indice_tarefa} atualizada para '{novo_nome_tarefa}'"
        else:
            return "Índice de tarefa inválido."
    except ValueError:
        return "Por favor, insira um número válido."

# Função para marcar uma tarefa como concluída
def completar_tarefa(tarefas, indice_tarefa):
    try:
        indice = int(indice_tarefa) - 1
        if 0 <= indice < len(tarefas):
            if tarefas[indice]["completada"]:
                return f"A tarefa {indice_tarefa} já está marcada como concluída."
            tarefas[indice]["completada"] = True
            return f"Tarefa {indice_tarefa} marcada como concluída."
        return "Índice de tarefa inválido."
    except ValueError:
        return "Por favor, insira um número válido."

# Função para deletar todas as tarefas que já foram concluídas
def deletar_tarefas_completadas(tarefas):
    tarefas_concluidas = [t for t in tarefas if t["completada"]]
    if not tarefas_concluidas:
        return "Nenhuma tarefa concluída para deletar."
    
    # Confirmação do usuário antes de apagar
    confirmar = input("Tem certeza que deseja deletar todas as tarefas concluídas? (s/n): ").strip().lower()
    if confirmar == "s":
        tarefas[:] = [t for t in tarefas if not t["completada"]]
        return "Tarefas concluídas deletadas com sucesso."
    return "Operação cancelada."

# Carrega as tarefas salvas (se houver) antes de iniciar
tarefas = carregar_tarefas()

# Loop principal do menu de opções
while True:
    print("\nMenu do Gerenciador de Lista de Tarefas:")
    print("1. Adicionar tarefas.")
    print("2. Ver tarefas.")
    print("3. Atualizar tarefas.")
    print("4. Completar tarefas.")
    print("5. Deletar tarefas concluídas.")
    print("6. Sair")

    escolha = input("\nDigite a opção desejada: ").strip()

    # Adiciona uma nova tarefa
    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
        print(adicionar_tarefa(tarefas, nome_tarefa))

    # Exibe todas as tarefas
    elif escolha == "2":
        ver_tarefas(tarefas)

    # Permite renomear uma tarefa
    elif escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja atualizar: ")
        novo_nome = input("Digite o novo nome da tarefa: ")
        print(atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome))

    # Marca uma tarefa como concluída
    elif escolha == "4":
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja completar: ")
        print(completar_tarefa(tarefas, indice_tarefa))

    # Deleta todas as tarefas concluídas
    elif escolha == "5":
        print(deletar_tarefas_completadas(tarefas))
        ver_tarefas(tarefas)

    # Encerra o programa, salvando as tarefas
    elif escolha == "6":
        salvar_tarefas(tarefas)
        print("Programa finalizado. Tarefas salvas com sucesso.")
        break

    else:
        print("Opção inválida. Tente novamente.")
