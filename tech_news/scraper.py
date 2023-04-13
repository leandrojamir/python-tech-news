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
        #  A função deve fazer o scrape do conteúdo recebido para obter uma
        # lista contendo as URLs das notícias listadas.
        #  Atenção: NÃO inclua a notícia em destaque da primeira página,
        # apenas as notícias dos cards.
        # <h2 class="entry-title">
        # <a href="https://blog.betrybe.com/tecnologia/website-development/"
        # rel="bookmark">Website development: o que é, o que faz e salário!
        # O guia inicial!</a></h2>
        urls_list = selector.css(".entry-title a::attr(href)").getall()
    except (requests.ReadTimeout, requests.HTTPError):
        return None

    # A função deve retornar esta lista.
    return urls_list


# 3 - Crie a função scrape_next_page_link
#  Para buscar mais notícias, precisaremos fazer a paginação, e para isto,
# vamos precisar do link da próxima página. Esta função será responsável por
# fazer o scrape deste link.
#  A função deve receber como parâmetro uma string contendo o conteúdo HTML da
# página de novidades (https://blog.betrybe.com)
# A função deve fazer o scrape deste HTML para obter a URL da próxima página.
def scrape_next_page_link(html_content):
    # URL_BASE = "http://books.toscrape.com/catalogue/"
    # # Vamos testar com a primeira página
    # response = requests.get(URL_BASE + "page-1.html")
    # selector = Selector(text=response.text)
    # # Recupera o atributo href do primeiro elemento que combine com o seletor
    # href = selector.css(".product_pod h3 a::attr(href)").get()
    # print(href)
    # # Para obter a url completa, basta adicionar a nossa URL_BASE
    # print(URL_BASE + href)
    URL_BASE = "https://blog.betrybe.com"
    # Caso não encontre o link da próxima página, a função deve retornar None
    try:
        selector = Selector(text=html_content)
        # <span aria-current="page" class="page-numbers current">1</span>
        page = selector.css(".page-numbers.current::text").get()
        print(f"\nestou na pagina:{page}")
    except (requests.HTTPError):
        return None
    if not page:
        return None
    else:
        next_page = int(page) + 1
    # A função deve retornar a URL obtida.
    print(f"{URL_BASE}/page/{str(next_page)}/")
    next_page_url = f"{URL_BASE}/page/{str(next_page)}/"
    return next_page_url


# tests/test_scraper.py::test_scrape_next_page_link
# estou na pagina:1
# https://blog.betrybe.com/page/2/

# estou na pagina:2
# https://blog.betrybe.com/page/3/

# estou na pagina:None
# PASSED


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
