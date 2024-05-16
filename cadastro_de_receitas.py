entrada = []
principal = []
sobremesa = []

# Menu de cadastro de receitas 
def cadastro_receitas():
    # Variáveis globais para serem utilzadas em outras funções
    global entrada, principal, sobremesa
    
    while True:
        print("\nCADASTRO DE RECEITAS:")
        selecao = int(input('''
        1 - Prato de Entrada
        2 - Prato Principal
        3 - Sobremesa
        4 - Cardápio
        4 - Quantidade de receitas cadastradas
        5 - Mostrar a lista
        6 - Continuar
        
        Selecione: '''))

        # Contagem das listas dos pratos para a quantidade
        if selecao == 4:
            print("Quantidade de receitas cadastradas:")
            print(f"Entrada: {len(entrada)} receitas")
            print(f"Principal: {len(principal)} receitas")
            print(f"Sobremesa: {len(sobremesa)} receitas")
            print()

        elif selecao == 5:
            print("Receitas cadastradas:")
            for tipo, receitas in [("Entrada", entrada), ("Principal", principal), ("Sobremesa", sobremesa)]:
                print(f"{tipo}: {len(receitas)} receitas")
                for receita in receitas:
                    print(receita)
                print()
            print()

        elif selecao == 6:
            print("\nSelecione no próximo menu:")
            # Def chamada para retornar ao menu principal depois de selecionar a opção 3 do submenu
            submenu_principal() 

        # Cadastro do prato
        elif selecao == 1 or selecao == 2 or selecao == 3:
            nome = input("\nInforme o nome do prato: ")
            pais = input("Informe o país de origem do prato: ")
            ingredientes = input("Informe os ingredientes para o prato: ")
            preparo = input("Escreva o modo de preparo: ")

            receita = {
                "Nome": nome,
                "País de origem": pais,
                "Ingredientes": ingredientes,
                "Modo de preparo": preparo
            }

            if selecao == 1:
                print("É uma entrada\n")
                entrada.append(receita)

            elif selecao == 2:
                print("É um prato principal\n")
                principal.append(receita)

            elif selecao == 3:
                print("É uma sobremesa\n")
                sobremesa.append(receita)

        else:
            print("Opção inválida!")

#  Função para o submenu de exclusão
def submenu_excluir(receitas):
    nome_prato = input("Informe o nome do prato que deseja excluir: ")
    for index, receita in enumerate(receitas):
        if receita["Nome"] == nome_prato:
            del receitas[index]
            print(f"Prato {nome_prato} excluído com sucesso!")
            return
    print(f"Prato {nome_prato} não encontrado.")

#  Função para o submenu de atualização
def submenu_atualizar(receitas):
    nome_prato = input("Informe o nome do prato que deseja atualizar: ")
    for receita in receitas:
        if receita["Nome"] == nome_prato:
            receita["País de origem"] = input("Informe o novo país de origem do prato: ")
            receita["Ingredientes"] = input("Informe os novos ingredientes para o prato: ")
            receita["Modo de preparo"] = input("Escreva o novo modo de preparo: ")
            print(f"Prato {nome_prato} atualizado com sucesso!")
            return
    print(f"Prato {nome_prato} não encontrado.")


def submenu_principal():
    global entrada, principal, sobremesa
    
    while True:
        # Adicionar um submenu em atualizar receitas
        # Selecione o que deseja atualizar:
        # 1 - Nome
        # 2 - País de origem
        # 3 - Ingredientes
        # 4 - Modo de preparo
        # 5 - Voltar
        submenu = int(input('''
        1 - Excluir receita
        2 - Atualizar receita
        3 - Voltar para o menu anterior
        4 - Finalizar o programa
        
        Selecione: '''))

        if submenu == 1:
            selecao = int(input('''
            1 - Entrada
            2 - Principal
            3 - Sobremesa
            
            Selecione o tipo de prato que deseja excluir: '''))
            if selecao == 1:
                submenu_excluir(entrada)
            elif selecao == 2:
                submenu_excluir(principal)
            elif selecao == 3:
                submenu_excluir(sobremesa)
            else:
                print("Opção inválida!")

        elif submenu == 2:
            selecao = int(input('''
            1 - Entrada
            2 - Principal
            3 - Sobremesa
            
            Selecione o tipo de prato que deseja atualizar: '''))
            if selecao == 1:
                submenu_atualizar(entrada)
            elif selecao == 2:
                submenu_atualizar(principal)
            elif selecao == 3:
                submenu_atualizar(sobremesa)
            else:
                print("Opção inválida!")

        elif submenu == 3:
            return

        elif submenu == 4:
            print("\nTenha um bom dia!")
            exit()

        else:
            print("\nOpção inválida!")


cadastro_receitas()