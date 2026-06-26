contatos = list()
indice_contatos = {}

def adicionar_contato(nome, telefone, email):
    if nome in indice_contatos:
        print(f"Contato com o nome '{nome}' já existe.")
        return
    contato = (nome, telefone, email)
    contatos.append(contato)
    indice_contatos[nome] = contato
    print(f"Contato '{nome}' adicionado com sucesso.")

def listar_contatos():
    if not contatos:
        print("Nenhum contato cadastrado.")
        return
    print("\nLista de contatos:")
    for c in contatos:
        print(f"Nome: {c[0]} | Telefone: {c[1]} | Email: {c[2]}")
    print()

def buscar_contato(nome):
    if nome in indice_contatos:
        contato = indice_contatos[nome]
        print(f"Contato encontrado: Nome: {contato[0]}, Telefone: {contato[1]}, Email: {contato[2]}")
    else:
        print(f"Contato '{nome}' não encontrado.")

def atualizar_contato(nome, novo_telefone, novo_email):
    if nome not in indice_contatos:
        print(f"Contato '{nome}' não encontrado.")
        return
    contato_atualizado = (nome, novo_telefone, novo_email)
    for i, c in enumerate(contatos):
        if c[0] == nome:
            contatos[i] = contato_atualizado
            break
    indice_contatos[nome] = contato_atualizado
    print(f"Contato '{nome}' atualizado com sucesso.")

def excluir_contato(nome):
    if nome not in indice_contatos:
        print(f"Contato '{nome}' não encontrado.")
        return
    contato = indice_contatos.pop(nome)
    contatos.remove(contato)
    print(f"Contato '{nome}' removido com sucesso.")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Buscar contato")
        print("4. Atualizar contato")
        print("5. Excluir contato")
        print("6. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            adicionar_contato(nome, telefone, email)

        elif escolha == '2':
            listar_contatos()

        elif escolha == '3':
            nome = input("Digite o nome do contato a buscar: ")
            buscar_contato(nome)

        elif escolha == '4':
            nome = input("Digite o nome do contato a atualizar: ")
            telefone = input("Novo telefone: ")
            email = input("Novo email: ")
            atualizar_contato(nome, telefone, email)

        elif escolha == '5':
            nome = input("Digite o nome do contato a excluir: ")
            excluir_contato(nome)

        elif escolha == '6':
            print("programa encerrado")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()