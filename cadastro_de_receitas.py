def cadastro_receitas():
    entrada = []
    principal = []
    sobremesa = []

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

        elif selecao_prato == 6:
            print("Tenha um bom dia!")
            break

        else:
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

cadastro_receitas()


# Criar uma def para excluir e outro para atualizar os pratos antes deles submenus. E dentro do primeiro Def vai enviar para o próximo def
# Exemplo: 1 para menu de exclusão; 2 para menu de atualização; 3 para voltar para o menu anterior; 4 para finalizar o programa.


submenu = int(input('''
     1 - Excluir receita
     2 - Atualizar receita
     3 - Voltar para o menu anterior
     4 - Finalizar o programa'''))
