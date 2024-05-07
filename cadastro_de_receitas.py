print("Cadastre aqui suas receitas por favor")
receita = []



# Função de cadastro de receitas: tipo_de_prato indica a refeição

def cadastro_receitas(receitas):
     tipo_de_prato = int(input('''Tipo de pratos:
        1 - Entrada
        2 - Prato Principal
        3 - Sobremesa
        Selecione: '''))     
     nome = input("Informe o nome da receita: ")
     pais = input("Informe o país de origem: ")
     ingredientes = input("Informe os ingredientes necessários: ").split('*')
     preparo = input("Descreva o modo de preparo: ")

     receita = {
          "nome" : nome,
          "País de Origem" : pais,
          "ingredientes" : ingredientes,
          "Modo de Preparo" : preparo
     }
     receitas.append(receita)
     print("Receita cadastrada com sucesso!")


