import requests
import time
from parsel import Selector


# 1 - Crie a função fetch
# A função deve receber uma URL
def fetch(url: str):
    #  Você vai precisar definir o header user-agent para que a raspagem do
    # blog da Trybe funcione corretamente. Para isso, preencha com o valor
    # "Fake user-agent" conforme exemplo abaixo:
    # { "user-agent": "Fake user-agent" }
    header = {"user-agent": "Fake user-agent"}
    try:
        #  A função deve fazer uma requisição HTTP get para esta URL
        # utilizando a função requests.get
        #  Caso a requisição não receba resposta em até 3 segundos, ela deve
        # ser abandonada (este caso é conhecido como "Timeout")
        response = requests.get(url, timeout=3, headers=header)
        # A função deve retornar o conteúdo HTML da resposta.
        response.raise_for_status()
        #  A função deve respeitar um Rate Limit de 1 requisição por segundo;
        # Ou seja, caso chamada múltiplas vezes, ela deve aguardar 1 segundo
        # entre cada requisição que fizer. Dica: Uma forma simples de garantir
        # que cada requisição seja feita com um intervalo mínimo de um segundo
        # é utilizar time.sleep(1) antes de cada requisição.
        # (Existem outras formas mais eficientes.)
        time.sleep(1)
    except (requests.ReadTimeout, requests.HTTPError):
        #  Caso a resposta tenha o código de status diferente de 200,
        # deve-se retornar None;
        # e a função deve retornar None.
        return None
    #  Caso a requisição seja bem sucedida com Status Code 200: OK, deve ser
    # retornado seu conteúdo de texto;
    return response.text


# 2 - Crie a função scrape_updates
#  Para conseguirmos fazer o scrape da página de uma notícia, primeiro
# precisamos de links para várias páginas de notícias. Estes links estão
# contidos na página inicial do blog da Trybe (https://blog.betrybe.com).
#  Esta função fará o scrape da página para obter as URLs das páginas de
# notícias. Vamos utilizar as ferramentas que aprendemos no curso, como a
# biblioteca Parsel, para obter os dados que queremos de cada página.
#  A função deve receber uma string com o conteúdo HTML da página inicial
# do blog
def scrape_updates(html_content):
    #  Caso não encontre nenhuma URL de notícia, a função deve retornar uma
    # lista vazia.
    urls_list = []
    try:
        # response = requests.get("http://books.toscrape.com/")
        # selector = Selector(text=response.text)
        selector = Selector(text=html_content)
        print(f"\n>selector:{selector}")
        #  A função deve fazer o scrape do conteúdo recebido para obter uma
        # lista contendo as URLs das notícias listadas.
        #  Atenção: NÃO inclua a notícia em destaque da primeira página,
        # apenas as notícias dos cards.
        # <h2 class="entry-title">
        # <a href="https://blog.betrybe.com/tecnologia/website-development/"
        # rel="bookmark">Website development: o que é, o que faz e salário!
        # O guia inicial!</a></h2>
        urls_list = selector.css(".entry-title a::attr(href)").getall()
        print(f"\n>selector:{urls_list}")
    except (requests.ReadTimeout, requests.HTTPError):
        return None

    # A função deve retornar esta lista.
    return urls_list


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
