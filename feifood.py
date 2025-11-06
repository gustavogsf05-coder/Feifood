def carregar_usuarios():
    usuarios = {}
    try:
        with open("dados_usuarios.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome, email, senha = linha.strip().split(";")
                usuarios[email] = {"nome": nome, "senha": senha}
    except FileNotFoundError:
        # Caso o arquivo ainda não exista
        pass
    return usuarios


def salvar_usuario(nome, email, senha):
    with open("dados_usuarios.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome};{email};{senha}\n")


def cadastrar_usuario(usuarios):
    print("\n=== Cadastro de novo usuário ===")
    nome = input("Digite seu nome: ").strip()
    email = input("Digite seu email: ").strip()
    senha = input("Digite sua senha: ").strip()

    if not nome or not email or not senha:
        print(" Todos os campos são obrigatórios! Tente novamente.\n")
        return

    if email in usuarios:
        print(" Este email já está cadastrado!\n")
        return

    salvar_usuario(nome, email, senha)
    usuarios[email] = {"nome": nome, "senha": senha}
    print(f" Usuário {nome} cadastrado com sucesso!\n")


def login_usuario(usuarios):
    print("\n=== Login de usuário ===")
    email = input("Digite seu email: ").strip()
    senha = input("Digite sua senha: ").strip()

    if email not in usuarios:
        print(" Email não encontrado. Tente novamente.\n")
        return

    if usuarios[email]["senha"] != senha:
        print(" Senha incorreta. Tente novamente.\n")
        return

    print(f" Bem-vindo(a), {usuarios[email]['nome']}!\n")


def main():
    usuarios = carregar_usuarios()

    while True:
        print("=== Menu Principal ===")
        print("1 - Cadastrar novo usuário")
        print("2 - Login de usuário")
        print("3 - Sair")

        opcao = input("Escolha uma opção (1, 2 ou 3): ").strip()

        if opcao == "1":
            cadastrar_usuario(usuarios)
        elif opcao == "2":
            login_usuario(usuarios)
        elif opcao == "3":
            print(" Encerrando o programa. Até logo!")
            break
        else:
            print(" Opção inválida! Tente novamente.\n")


if __name__ == "__main__":
    main()
