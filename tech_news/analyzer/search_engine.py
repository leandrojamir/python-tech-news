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

    return tuple_list


# 8 - Crie a função search_by_date
# Esta função irá buscar as notícias do banco de dados por data.
# A função deve receber como parâmetro uma data no formato ISO AAAA-mm-dd
# A função deve buscar as notícias do banco de dados por data.
# A função deve ter retorno no mesmo formato do requisito anterior.
#  Caso a data seja inválida, ou esteja em outro formato, uma exceção
# ValueError deve ser lançada com a mensagem Data inválida.
# Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.
#  Lembre-se: A função recebe uma data no formato ISO AAAA-mm-dd, mas no banco
# a data está salva no formato dd/mm/AAAA. Dica: Lembrem-se de como
# trabalhamos com datas nos projetos anteriores.
def search_by_date(date):
    """Seu código deve vir aqui"""


# 9 - Crie a função search_by_category
# Esta função irá buscar as notícias por categoria.
# A função deve receber como parâmetro o nome da categoria completo.
def search_by_category(category):
    # A função deve buscar as notícias do banco de dados por categoria.
    print(f"\nvvv\nbusca pela categoria:{category}")
    query = {
        "category": {
            "$regex": f"{category}",
            # A busca deve ser case insensitive
            "$options": "i",
        },
    }
    # Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.
    tuple_list = []
    data_with_query = search_news(query)
    # A função deve ter retorno no mesmo formato do requisito anterior.
    for info in data_with_query:
        tuple_list.append((info["title"], info["url"]))

    return tuple_list
