def menu_principal():
    while True:
        print("\nBem vindo ao Feifood")
        print("=== Menu principal ===")
        print("1 - Cadastro")
        print("2 - Login")
        print("3 - Sair")
        
        escolha_1 = input("Selecione uma opção: ").strip()
        print(f"[DEBUG] Você digitou: '{escolha_1}'")

        if escolha_1 == "1":
            cadastrar()

        elif escolha_1 == "2":
            resultado = login()
            if resultado:
                usuario = resultado  
                while True:
                    print(f"\n{usuario}, bem-vindo ao Feifood!\n")
                    print("PESQUISAR  - Pesquisar alimentos")
                    print("HISTORICO  - Ver histórico de pesquisas")
                    print("PEDIDOS    - Cadastrar pedido")
                    print("AVALIAR    - Avaliar pedidos")
                    print("SAIR       - Voltar ao menu principal")

                    escolha_2 = input("Selecione uma opção: ").strip().upper()
                    print(f"[DEBUG] Você digitou: '{escolha_2}'\n")

                    if escolha_2 == "PESQUISAR":
                        pesquisar(usuario)
                    elif escolha_2 == "HISTORICO":
                        historico(usuario)   
                    elif escolha_2 == "PEDIDOS":
                        pedidos(usuario)
                    elif escolha_2 == "AVALIAR":
                        avaliar(usuario)
                    elif escolha_2 == "SAIR":
                        break
                    else:
                        print("Informação inválida! Tente novamente.")

        elif escolha_1 == "3":
            print("Saindo do aplicativo...")
            break

        else:
            print("Informação inválida! Tente novamente.")



def cadastrar():
    print("\n=== Menu de cadastro ===")
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite uma senha: ")

    with open("dados_usuarios.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha or ";" not in linha:
                continue
            nome, _ = linha.split(";")
            if nome == usuario:
                print("Usuário já existente. Tente novamente.\n")
                return
            
    with open("dados_usuarios.txt", "a") as arquivo:
        arquivo.write(f"{usuario};{senha}\n")
        print(f"Usuário {usuario} cadastrado com sucesso!\n")



def login():
    print("\n=== Efetue o login ===")
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

    with open("dados_usuarios.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha or ";" not in linha:
                continue
            nome_arquivo, senha_arquivo = linha.split(";")
            if nome_arquivo == usuario and senha_arquivo == senha:
                return nome_arquivo
    print("Usuário ou senha incorretos. Tente novamente.\n")
    return False



def pesquisar(usuario):
    print("-= Área de pesquisa =-")
    while True:
        alimento = input("O que está procurando hoje? (SAIR para voltar)\n> ").strip()

        if alimento.upper() == "SAIR":
            print("Voltando para o menu...")
            break
        with open ("_historico.txt","a") as historico:
            historico.write(f"{usuario};{alimento}\n")

        encontrado = False
        with open("_alimentos.txt", "r") as arquivo:  
            for linha in arquivo:
                partes = linha.strip().split(";")  
                nome_alimento = partes[0]
                sabores = partes[1:]

                if alimento.lower() == nome_alimento.lower():
                    print(f"Resultados para: {nome_alimento}")
                    print(f"Sabores: {' | '.join(sabores)}")
                    encontrado = True

                    escolha_3 = input("Deseja realizar um pedido? (S/N): ").strip().upper()
                    if escolha_3 == "S":
                        pedidos(usuario)
                    break  
            
        if not encontrado:   
            print("Nenhum resultado encontrado :/")


def historico(usuario):
    print(f"\nHistorico de pesquisa")
    with open("_historico.txt","r") as arquivo:
        for linha in arquivo:
            nome, alimentos =linha.strip().split(';')
            print(f"-{alimentos}")

def pedidos(usuario):
    while True:
        print("\nMenu de pedidos\n")
        print("CRIAR - cria pedido")
        print("EDITAR - editar pedido")
        print("EXCLUIR - excluir pedido")
        print("VER PEDIDOS - lista de pedidos")
        print("SAIR - Voltar ao menu principal")
        escolha_4 = input("Selecione uma opção: ").strip().upper()

        if escolha_4 == "CRIAR":
            criar_pedido(usuario)
        elif escolha_4 == "EDITAR":
            editar_pedido()
        elif escolha_4 == "EXCLUIR":
            excluir_pedido()
        elif escolha_4 == "VER PEDIDOS":
            ver_pedidos(usuario)
        elif escolha_4 == "SAIR":
            break
        else:
            print("Informação inválida! Tente novamente.")

def criar_pedido(usuario):
    alimento = input("Alimento: ").strip()
    quantidade = int(input("Quantidade: ").strip())
    sabores = [input(f"Sabor {i+1}: ").strip() for i in range(quantidade)]

    # Gerar ID
    try:
        with open("_pedidos.txt", "r") as f:
            ultimo_id = int(f.readlines()[-1].split(";")[0])
    except:
        ultimo_id = 0

    novo_id = ultimo_id + 1

    with open("_pedidos.txt", "a") as f:
        f.write(f"{novo_id};{usuario};{alimento};{','.join(sabores)};{quantidade}\n")
    print(f"Pedido criado! ID: {novo_id}")



def ver_pedidos(usuario):
    try:
        with open("_pedidos.txt", "r") as f:
            for linha in f:
                id_p, nome, alimento, sabores, quantidade = linha.strip().split(";")
                if nome == usuario:
                    print(f"ID:{id_p} | {alimento} | Sabores:{sabores} | Qt:{quantidade}")
    except:
        print("Nenhum pedido registrado.")


def avaliar(usuario):
    print(f"\nPedidos de {usuario}:")
    ver_pedidos(usuario)

    id_pedido = input("Digite o ID do pedido que deseja avaliar: ").strip()
    
    while True:
        nota = input("Digite a nota de 1 a 5: ").strip()
        if nota.isdigit() and 1 <= int(nota) <= 5:
            break
        print("Nota inválida! Digite um número de 0 a 5.")

    with open("_avaliacoes.txt", "a") as arquivo:
        arquivo.write(f"{usuario};{id_pedido};{nota}\n")
    
    print(f"Pedido '{id_pedido}' avaliado com nota {nota} com sucesso!")

def excluir_pedido():
    usuario = input("Usuário: ").strip()
    ver_pedidos(usuario)
    id_exc = input("ID do pedido a excluir: ").strip()

    with open("_pedidos.txt", "r") as f:
        linhas = f.readlines()

    with open("_pedidos.txt", "w") as f:
        f.writelines(l for l in linhas if l.strip().split(";")[0] != id_exc)
    print("Pedido excluído!")


menu_principal()
