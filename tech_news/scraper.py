import requests
import time


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
        print(f"\n>res:{response}")
        # A função deve retornar o conteúdo HTML da resposta.
        print(f"\n>raise http error:{response.raise_for_status}")
        print(f"\n>text:{response.text}")
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
    print(f"\n>200 content text:{response.text}")
    #  Caso a requisição seja bem sucedida com Status Code 200: OK, deve ser
    # retornado seu conteúdo de texto;
    return response.text


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
