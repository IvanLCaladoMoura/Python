import json

ARQUIVO_CONTATOS = "contatos.json"

# Função para salvar a lista de contatos em um arquivo JSON
def salvar_contatos(contatos, nome_arquivo=ARQUIVO_CONTATOS):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(contatos, f, ensure_ascii=False, indent=4)

# Função para carregar a lista de contatos de um arquivo JSON
def carregar_contatos(nome_arquivo=ARQUIVO_CONTATOS):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        # Retorna lista vazia se o arquivo ainda não existir
        return []

# 1 Função para adicionar um novo contato
def adicionar_contato(contatos):
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("Email: ").strip()

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favoritos": False
    }

    contatos.append(contato)
    salvar_contatos(contatos)
    return f"Contato '{nome}' adicionado com sucesso!"

# 2 Função para exibir todos os contatos na tela
def ver_contatos(contatos):
    print("\nLista de Contatos:")
    if not contatos:
        print("Nenhum contato cadastrado.")
    else:
        for i, contato in enumerate(contatos, start=1):
            fav = "⭐" if contato.get("favoritos") else ""
            print(f"{i}. {fav} Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")

# 3 Função para  atualizar os contatos       
def atualizar_contato(contatos, indice_contato, campo, novo_valor):
    try:
        indice = int(indice_contato) - 1
        if 0 <= indice < len(contatos):
            campo = campo.lower()
            if campo in ["nome", "telefone", "email"]:
                contatos[indice][campo] = novo_valor.strip()
                salvar_contatos(contatos)
                return f"{campo.capitalize()} do contato {indice_contato} atualizado para '{novo_valor}'"
            else:
                return "Campo inválido. Escolha entre 'nome', 'telefone' ou 'email'."
        else:
            return "Índice de contato inválido."
    except ValueError:
        return "Por favor, insira um número válido."
    
# 4 Função para marcar um contato como favorito
def favoritos(contatos, indice_contato):
    try:
        indice = int(indice_contato) - 1
        if 0 <= indice < len(contatos):
            contato = contatos[indice]
            #Alterna o estado do campo "Favoritos"
            if contato.get("favoritos"):
                contato["favoritos"] = False
                mensagem = f"Contato '{contato['nome']}' removido dos favoritos."
            else:
                contato["favoritos"] = True
                mensagem = f"Contato  '{contato['nome']}'marcado como favorito.  "
            salvar_contatos(contatos)
            return mensagem
        else:
            return "Indice de contato inválido."
    except ValueError:
        return "Por favor, insira um número válido. "

    
# 5 Função para exibir todos os favoritos na tela
def ver_favoritos(contatos):
    favoritos = [c for c in contatos if c.get("favoritos")]
    print("\n⭐ Favoritos:")
    if not favoritos:
        print("Nenhum contato favorito cadastrado.")
    else:
        for i, contato in enumerate(favoritos, start=1):
            print(f"{i}. Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")

# 6 Função para deletar os contatos
def deletar_contato(contatos, indice_contato):
    try:
        indice = int(indice_contato) - 1
        if 0 <= indice < len(contatos):
            removido = contatos.pop(indice)
            salvar_contatos(contatos)
            return f"Contato '{removido['nome']}' removido com sucesso. "
        else:
            return "Índice de contato inválido. "
    except ValueError:
        return "Por favor, insira um número válido."
    
# Carrega contatos ao iniciar
contatos = carregar_contatos()

# Loop principal do menu de opções
while True:
    print("\n☎︎  Menu Contatos do Usuário: ")
    print("1. Adicionar Contatos.")
    print("2. Ver Contatos.")
    print("3. Atualizar Contatos.")
    print("4. Salvar em Favoritos.")
    print("5. Ver Favoritos.")
    print("6. Deletar um Contato.")
    print("7. Sair")

    escolha = input("\nDigite a opção desejada: ").strip()

    # Caso o usuário escolha cada uma das opções
    if escolha == "1":
        print(adicionar_contato(contatos))
    elif escolha == "2":
        ver_contatos(contatos)
    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja atualizar: ")
        campo = input("Qual campo deseja atualizar? (nome, telefone, e-mail): ")
        novo_valor = input(f"Digite o novo valor para {campo}: ")
        print(atualizar_contato(contatos, indice_contato, campo, novo_valor))
        print("\nAtualização realizada com sucesso.")
    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja marcar/desmarcar como favorito: ")
        print(favoritos(contatos, indice_contato))
    elif escolha == "5":
        ver_favoritos(contatos)
    elif escolha == "6":
        ver_contatos(contatos)
        indice = input("Número do contato a deletar: ")
        print(deletar_contato(contatos, indice))
    elif escolha == "7":
        # Salva os contatos antes de encerrar
        salvar_contatos(contatos)
        print("📁 Contatos salvos. Programa encerrado.")
        break
    else:
        print("⚠︎ Opção inválida. Tente novamente.")