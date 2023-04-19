# 10 - Crie a função top_5_categories
#  Esta função irá listar as cinco categorias com maior ocorrência no banco de
# dados.
from tech_news.database import find_news


def top_5_categories():
    # A função deve buscar as categorias do banco de dados
    category = find_news()
    # e calcular a sua "popularidade" com base no número de ocorrências;
    category_list = {}
    for info in category:
        category_info = info["category"]
        print(f"\nCategorias: {category_info}")
        if category_info in category_list:
            category_list[category_info] = category_list[category_info] + 1
        else:
            category_list[category_info] = 1
    print(f"\nvvv\nLista com ocorrencias: {category_list}")

    #  A ordem das categorias retornadas deve ser da mais popular para a menos
    # popular, ou seja, categorias que estão em mais notícias primeiro;
    # Em caso de empate, o desempate deve ser por ordem alfabética de categoria
    def tupla_list_item(category_info):
        return (-category_info[1], category_info[0])
    category_list_sorted = sorted(category_list.items(), key=tupla_list_item)
    print(f"\nvvv\nLista em ordem: {category_list_sorted}")

    #  As top 5 categorias da análise devem ser retornadas em uma lista no
    # formato ["category1", "category2"];
    #  Caso haja menos de cinco categorias, no banco de dados, deve-se retornar
    # todas as categorias existentes;
    # Caso não haja categorias disponíveis, deve-se retornar uma lista vazia.
    top_5_list = []
    for category_info, _ in category_list_sorted[0:5]:
        top_5_list.append(category_info)
    print(f"\nvvv\napenas até 5 primeiras: {top_5_list}")
    return top_5_list
