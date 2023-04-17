# 7 - Crie a função search_by_title
# local: tech_news/analyzer/search_engine.py
#  Além de testar funcionalidades que acessam o banco, podemos fazer as nossas
# próprias funcionalidades! Esta função irá fazer buscas por título.
#  Lembre-se; para acesso ao banco de dados importe db definido no módulo
# tech_news/database.py.
from tech_news.database import search_news


# A função deve receber uma string com um título de notícia
def search_by_title(title: str):
    # A função deve buscar as notícias do banco de dados por título
    query = {
        "title": {
            "$regex": f"{title}",
            # A busca deve ser case insensitive
            "$options": "i",
        },
    }
    print(f"\nvvv\nbusca pelo titulo:{title}")
    print(f"\nvvv\nbusca no mongoDB com a query:{query}")
    # Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.
    tuple_list = []
    # A função deve buscar as notícias do banco de dados por título
    #  A função deve retornar uma lista de tuplas com as notícias encontradas
    # nesta busca. Exemplo:
    # [
    #   ("Título1_aqui", "url1_aqui"),
    #   ("Título2_aqui", "url2_aqui"),
    #   ("Título3_aqui", "url3_aqui"),
    # ]
    data_with_query = search_news(query)
    for info in data_with_query:
        tuple_list.append((info["title"], info["url"]))
    print(f"\nvvv\nresultado das buscas{tuple_list}")

    return tuple_list


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
