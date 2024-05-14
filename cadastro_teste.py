import os

entrada = []
principal = []
sobremesa = []

def cadastro_receitas():
    global entrada, principal, sobremesa
    
    while True:
        print("Cadastro de Receitas")
        selecao_prato = int(input('''
        1 - Prato de Entrada
        2 - Prato Principal
        3 - Sobremesa
        4 - Quantidade de receitas cadastradas
        5 - Mostrar a lista
        6 - Sair
        
        Selecione: '''))

        if selecao_prato == 4:
            print("Quantidade de receitas cadastradas:")
            print(f"Entrada: {len(entrada)} receitas")
            print(f"Principal: {len(principal)} receitas")
            print(f"Sobremesa: {len(sobremesa)} receitas")
            print()

        elif selecao_prato == 5:
            print("Receitas cadastradas:")
            for tipo, receitas in [("Entrada", entrada), ("Principal", principal), ("Sobremesa", sobremesa)]:
                print(f"{tipo}: {len(receitas)} receitas")
                for receita in receitas:
                    print(receita)
                print()
            print()

        elif selecao_prato == 6:
            print("Tenha um bom dia!")
            break

        elif selecao_prato == 1 or selecao_prato == 2 or selecao_prato == 3:
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

            if selecao_prato == 1:
                print("É uma entrada\n")
                entrada.append(receita)

            elif selecao_prato == 2:
                print("É um prato principal\n")
                principal.append(receita)

            elif selecao_prato == 3:
                print("É uma sobremesa\n")
                sobremesa.append(receita)

        else:
            print("Opção inválida!")

def submenu_excluir(receitas):
    nome_prato = input("Informe o nome do prato que deseja excluir: ")
    for index, receita in enumerate(receitas):
        if receita["Nome"] == nome_prato:
            del receitas[index]
            print(f"Prato {nome_prato} excluído com sucesso!")
            return
    print(f"Prato {nome_prato} não encontrado.")

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
        submenu = int(input('''
        1 - Excluir receita
        2 - Atualizar receita
        3 - Voltar para o menu anterior
        4 - Finalizar o programa
        
        Selecione: '''))

        if submenu == 1:
            selecao_prato = int(input('''
            1 - Entrada
            2 - Principal
            3 - Sobremesa
            
            Selecione o tipo de prato que deseja excluir: '''))
            if selecao_prato == 1:
                submenu_excluir(entrada)
            elif selecao_prato == 2:
                submenu_excluir(principal)
            elif selecao_prato == 3:
                submenu_excluir(sobremesa)
            else:
                print("Opção inválida!")

        elif submenu == 2:
            selecao_prato = int(input('''
            1 - Entrada
            2 - Principal
            3 - Sobremesa
            
            Selecione o tipo de prato que deseja atualizar: '''))
            if selecao_prato == 1:
                submenu_atualizar(entrada)
            elif selecao_prato == 2:
                submenu_atualizar(principal)
            elif selecao_prato == 3:
                submenu_atualizar(sobremesa)
            else:
                print("Opção inválida!")

        elif submenu == 3:
            break

        elif submenu == 4:
            print("Tenha um bom dia!")
            exit()

        else:
            print("Opção inválida!")


cadastro_receitas()
submenu_principal()

def cardapio():
     
    ent = int(input("Monte seu cardápio! Quantas entradas você deseja? "))
    prin = int(input("Quantos pratos principais? "))
    sob = int(input("Quantas sobremesas? "))

    for i in range (ent):
        index = int.from_bytes(os.urandom(1), "little") % len(entrada)
        recipe_ent = entrada[index]

        print(recipe_ent)

    for i in range (prin):
        index = int.from_bytes(os.urandom(1), "little") % len(principal)
        recipe_prin = principal[index]

        print(recipe_prin)

    for i in range (sob):
        index = int.from_bytes(os.urandom(1), "little") % len(sobremesa)
        recipe_sob = sobremesa[index]

        print(recipe_sob)

    sugestao = input("Deseja outra sugestão aleatória de cardápio? Digite 'sim' ou 'não': ")

    if sugestao == 'sim':
        cardapio()
