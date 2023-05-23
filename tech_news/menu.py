# Requisitos bônus
# 11 - Crie a função analyzer_menu
# local: tech_news/menu.py
#  Esta função é o menu do nosso programa. Através dele poderemos operar as
# funcionalidades que criamos. Será um menu de opções, em que cada opção pede
# as informações necessárias para disparar uma ação.
import sys


# 'analyzer_menu' is too complex (8)Flake8(C901)
def analyzer_menu():
    menu_option = ""
    # O texto exibido pelo menu deve ser exatamente:
    # Selecione uma das opções a seguir:
    #  0 - Popular o banco com notícias;
    #  1 - Buscar notícias por título;
    #  2 - Buscar notícias por data;
    #  3 - Buscar notícias por categoria;
    #  4 - Listar top 5 categorias;
    #  5 - Sair.

    if menu_option != "5":
        menu_option = input(
            "Selecione uma das opções a seguir:\n"
            " 0 - Popular o banco com notícias;\n"
            " 1 - Buscar notícias por título;\n"
            " 2 - Buscar notícias por data;\n"
            " 3 - Buscar notícias por categoria;\n"
            " 4 - Listar top 5 categorias;\n"
            " 5 - Sair."
        )
#  A função input deve ser utilizada para receber a entrada de dados da pessoa
# usuária.
        match menu_option:
            #  Caso a opção 0 seja selecionada, seve-se exibir a mensagem
            # "Digite quantas notícias serão buscadas:"
            case "0":
                print("Digite quantas notícias serão buscadas: ")
            #  Caso a opção 1 seja selecionada, deve-se exibir a mensagem
            # "Digite o título:";
            case "1":
                print("Digite o título: ")
            #  Caso a opção 2 seja selecionada, deve-se exibir a mensagem
            # "Digite a data no formato aaaa-mm-dd:";
            case "2":
                print("Digite a data no formato aaaa-mm-dd: ")
            #  Caso a opção 3 seja selecionada, deve-se exibir a mensagem
            # "Digite a categoria:";
            case "3":
                print("Digite a categoria: ")
            case "4":
                print("Opção 4")
            case "5":
                print("Opção 5")
            #  Caso a opção não exista, exiba a mensagem de erro
            # "Opção inválida" na stderr.
            case _:
                sys.stderr.write("Opção inválida\n")
