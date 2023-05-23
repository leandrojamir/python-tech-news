# Requisitos bônus
# 11 - Crie a função analyzer_menu
# local: tech_news/menu.py
#  Esta função é o menu do nosso programa. Através dele poderemos operar as
# funcionalidades que criamos. Será um menu de opções, em que cada opção pede
# as informações necessárias para disparar uma ação.

# 12 - Implemente as funcionalidades do menu
# local: tech_news/menu.py
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_title,
)
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
        #  A função input deve ser utilizada para receber a entrada de dados
        # da pessoa usuária.
        #  Quando selecionada uma opção do menu, e inseridas as informações
        # necessárias, a ação adequada deve ser realizada.

        match menu_option:
            #  Caso a opção 0 seja selecionada, seve-se exibir a mensagem
            # "Digite quantas notícias serão buscadas:"
            #  Caso a opção 0 seja selecionada, a função get_tech_news deve
            # ser importada;
            case "0":
                get_tech_news(
                    int(input("Digite quantas notícias serão buscadas: "))
                )
            #  Caso a opção 1 seja selecionada, deve-se exibir a mensagem
            # "Digite o título:";
            #  Caso a opção 1 seja selecionada, a função search_by_title deve
            # ser importada e seu resultado deve ser impresso em tela;
            case "1":
                search_by_title(input("Digite o título: "))
            #  Caso a opção 2 seja selecionada, deve-se exibir a mensagem
            # "Digite a data no formato aaaa-mm-dd:";
            #  Caso a opção 2 seja selecionada, a função search_by_date deve
            # ser importada e seu resultado deve ser impresso em tela;
            case "2":
                search_by_date(input("Digite a data no formato aaaa-mm-dd: "))
            #  Caso a opção 3 seja selecionada, deve-se exibir a mensagem
            # "Digite a categoria:";
            #  Caso a opção 3 seja selecionada, a função search_by_category
            # deve ser importada e seu resultado deve ser impresso em tela;
            case "3":
                search_by_category(input("Digite a categoria: "))
            #  Caso a opção 4 seja selecionada, a função top_5_categories deve
            # ser importada e seu resultado deve ser impresso em tela;
            case "4":
                top_5_categories()
            #  Caso a opção 5 seja selecionada, deve-se encerrar a execução do
            # script e exibir a mensagem "Encerrando script";
            case "5":
                print("Encerrando script")
            #  Caso a opção não exista, exiba a mensagem de erro
            # "Opção inválida" na stderr.
            #  Caso alguma exceção seja lançada, a mesma deve ser capturada e
            # sua mensagem deve ser exibida na saída padrão de erros (stderr).
            case _:
                sys.stderr.write("Opção inválida\n")
