# 1 - Crie a função fetch
# local: tech_news/scraper.py
#  Antes de fazer scrape, precisamos de uma página! Esta função será
# responsável por fazer a requisição HTTP ao site e obter o conteúdo HTML.
#  Alguns cuidados deverão ser tomados: como a nossa função poderá ser
# utilizada várias vezes em sucessão, na nossa implementação devemos nos
# assegurar que um Rate Limit será respeitado.
#  A função deve receber uma URL
#  A função deve fazer uma requisição HTTP get para esta URL utilizando a
# função requests.get
#  A função deve retornar o conteúdo HTML da resposta.
#  A função deve respeitar um Rate Limit de 1 requisição por segundo; Ou seja,
# caso chamada múltiplas vezes, ela deve aguardar 1 segundo entre cada
# requisição que fizer. Dica: Uma forma simples de garantir que cada
# requisição seja feita com um intervalo mínimo de um segundo é utilizar
# time.sleep(1) antes de cada requisição.
# (Existem outras formas mais eficientes.)
#  Caso a requisição seja bem sucedida com Status Code 200: OK, deve ser
# retornado seu conteúdo de texto;
#  Caso a resposta tenha o código de status diferente de 200,
# deve-se retornar None;
#  Caso a requisição não receba resposta em até 3 segundos, ela deve ser
# abandonada (este caso é conhecido como "Timeout") e a função
# deve retornar None.
#  Você vai precisar definir o header user-agent para que a raspagem do blog
# da Trybe funcione corretamente. Para isso, preencha com o valor
# "Fake user-agent" conforme exemplo abaixo:
# { "user-agent": "Fake user-agent" }
def fetch(url):
    """Seu código deve vir aqui"""


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
