arquivo = open("arquivo_receitas.txt", "a+")
import random

entrada = []
principal = []
sobremesa = []
receitas = []

# Menu de cadastro de receitas 
def cadastro_receitas():
    # Variáveis globais para serem utilzadas em outras funções
    global entrada, principal, sobremesa
    global nome, pais, ingredientes, preparo
    
    while True:
        print("\nCADASTRO DE RECEITAS:")
        selecao = int(input('''
        1 - Prato de Entrada
        2 - Prato Principal
        3 - Sobremesa
        4 - Cardápio
        5 - Quantidade de receitas cadastradas
        6 - Mostrar a lista
        7 - Filtrar receitas por país                    
        8 - Continuar
        
        Selecione: '''))

        # Entrada para o menu de cardápio
        if selecao == 4:
            cardapio()

        # Contagem das listas dos pratos para a quantidade
        elif selecao == 5:
            print("Quantidade de receitas cadastradas:")
            print(f"Entrada: {len(entrada)} receitas")
            print(f"Principal: {len(principal)} receitas")
            print(f"Sobremesa: {len(sobremesa)} receitas")
            print()
    
        # Lógica de print das receitas cadastradas pelo usuário
        elif selecao == 6:
            print("Receitas cadastradas:")
            for tipo, receitas in [("Entrada", entrada), ("Principal", principal), ("Sobremesa", sobremesa)]:
                print(f"{tipo}: {len(receitas)} receitas")
                for receita in receitas:
                    print(receita)
                print()
            print()

        elif selecao == 7:
            print("Filtrar receitas por país de origem:")    
            # Def chamada para filtrar receitas por país
            filtrar_receitas(receitas)  

        # Entrada para o menu seguinte
        elif selecao == 8:
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

            receitas.append(receita)

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

#Salvando dados cadastrados em arquivo de formato .txt
def salvar_receitas(receitas):    
    with open("arquivo_receitas.txt", "r+") as arquivo:
        for receita in receitas:
            arquivo.write(f"Nome do prato: {nome}\n")
            arquivo.write(f"País: {pais} \n")
            arquivo.write(f"Ingredientes: {ingredientes} \n")
            arquivo.write(f"Modo de preparo: {preparo} \n")
            arquivo.write("\n\n")
            print("Dados salvos com sucesso!")

# Função para filtrar receitas
def filtrar_receitas(receitas):
    with open("arquivo_receitas.txt", "r"):
        pais = input("Informe o país: ")
        for receita in receitas:
            if receita[pais] == pais:
                receitas_filtradas = []
                receitas_filtradas.append(receita)
    return receitas_filtradas()

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
            escolha = int(input('''O que deseja atualizar?
                        1 - Nome
                        2 - País
                        3 - Ingredientes
                        4 - Modo de preparo
                                
                        selecione: '''))
            if escolha == 1:
                receita["Nome"] = input("Informe o novo nome do prato: ")
            if escolha == 2:
                receita["País de origem"] = input("Informe o novo país de origem do prato: ")
            if escolha == 3:
                receita["Ingredientes"] = input("Informe os novos ingredientes do prato: ")
            if escolha == 4:
                receita["Modo de preparo"] = input("Informe o novo modo de preparo prato: ")
            print(f"\nPrato {nome_prato} atualizado com sucesso!")
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
            selecao = int(input('''\nExcluir prato:
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
            selecao = int(input('''\nAtualizar prato:
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


def cardapio(): 
    
    while True: 
        ent = int(input("\nMonte seu cardápio! Quantas entradas você deseja? "))
        prin = int(input("Quantos pratos principais? "))
        sob = int(input("Quantas sobremesas? "))

        if ent > len(entrada):
            print("Não há entradas cadastradas o suficiente!")
            ent = len(entrada)

        if prin > len(principal):
            print("Não há pratos principais cadastrados o suficiente!")
            prin = len(principal)

        if sob > len(sobremesa):
            print("Não há sobremesas cadastradas o suficiente!")
            sob = len(sobremesa)

        recipe_ent = random.sample(entrada, ent)
        recipe_prin = random.sample(principal, prin)
        recipe_sob = random.sample(sobremesa, sob)

        print("Cardápio:\n")
        print(f"""Entradas: {recipe_ent}\n
        Pratos Principais: {recipe_prin}\n
        Sobremesas: {recipe_sob}""")

        sugestao = input("Você deseja outro cardápio? Digite sim ou não: ")

        if sugestao == 'nao':
            break

salvar_receitas(receitas)

cadastro_receitas()