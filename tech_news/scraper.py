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
    except (requests.HTTPError):
        return None
    if not page:
        return None
    else:
        next_page = int(page) + 1
    # A função deve retornar a URL obtida.
    next_page_url = f"{URL_BASE}/page/{str(next_page)}/"
    return next_page_url


# 4 - Crie a função scrape_news
#  Agora que sabemos pegar páginas HTML, e descobrir o link de notícias,
# é hora de fazer o scrape dos dados que procuramos!
# É bom saber que ao fazer scraping na vida real, você está sempre "refém" de
# quem construiu o site. Por exemplo, pode ser que nem toda notícia tenha
# exatamente o mesmo HTML/CSS e você precise de criatividade para contornar.
#  A função deve receber como parâmetro o conteúdo HTML da página de uma
# única notícia
def scrape_news(html_content):
    selector = Selector(text=html_content)
    #  A função deve, no conteúdo recebido, buscar as informações das notícias
    # para preencher um dicionário com os seguintes atributos:
    # url - link para acesso da notícia.
    # <link rel="canonical" href="https://blog.betrybe.com/tecnologia/
    # cabos-de-rede/">
    url = selector.css("link[rel='canonical']::attr(href)").get()
    print(f"\n'url': '{url}'")
    # title - título da notícia.
    # <h1 class="entry-title">Cabos de rede: o que são, quais os tipos e como
    # crimpar?</h1>
    title = selector.css(".entry-title::text").get()
    print(f"\n'title': '{title}'")
    # timestamp - data da notícia, no formato dd/mm/AAAA.
    # <li class="meta-date">10/04/2023</li>
    timestamp = selector.css(".meta-date::text").get()
    print(f"\n'timestamp': '{timestamp}'")
    # writer - nome da pessoa autora da notícia.
    # <a class="url fn n" href="https://blog.betrybe.com/author/dayane-arena
    # -dos-santos/" title="View all posts by Dayane Arena dos Santos">Dayane
    # Arena dos Santos</a>
    writer = selector.css(".url.fn.n::text").get()
    print(f"\n'writer': '{writer}'")
    # reading_time - número de minutos necessários para leitura.
    # <li class="meta-reading-time"><i class="cs-icon cs-icon-clock"></i>
    # 9 minutos de leitura</li>
    reading_time = selector.css(".meta-reading-time::text").get().split()[0]
    print(type(reading_time))
    reading_time_int = int(reading_time)
    print(f"\n'reading_time': '{reading_time}'")
    # 'reading_time': '5 minutos de leitura'
    # 'reading_time': '['15', 'minutos', 'de', 'leitura']'
    # summary - o primeiro parágrafo da notícia.
    # #main > article > div > div.entry-content-wrap > div.entry-content >
    # p:nth-child(1)
    # <div class="entry-content">
    # <p>...</p>
    summary = selector.css(
        # dica do Isaac https://www.w3schools.com/cssreF/css_selectors.php
        # https://www.w3schools.com/cssreF/sel_first-of-type.php
        # :first-of-type	p:first-of-type	Selects every <p> element that
        # is the first <p> element of its parent
        #  Caso uma tag possua outras tags aninhadas, você pode usar o
        # seletor * para obter informações da tag ancestral e também de
        # suas tags descendentes.
        "div.entry-content:first-of-type > p:first-of-type *::text"
    ).getall()
    # https://www.youtube.com/watch?v=vuLNc2yCNYk 16:52 // 35:34 //p//text()
    # //*[@id="main"]/article/div/div[2]/div[1]/p[1]/text()[1]
    # summary = selector.xpath("//p[1][text()]").get()
    print(f"\n'summary': '{summary}'")
    # só esta passando com getall porem recebo lista de paragrafos
    # 'summary': '['Desde o surgimento do computador e seus respectivos
    # category - categoria da notícia.
    category = selector.css(".category-style .label::text").get()
    # Exemplo de um retorno da função com uma notícia fictícia:
    # {
    #   "url": "https://blog.betrybe.com/novidades/noticia-bacana",
    #   "title": "Notícia bacana",
    #   "timestamp": "04/04/2021",
    #   "writer": "Eu",
    #   "reading_time": 4,
    #   "summary": "Algo muito bacana aconteceu",
    #   "category": "Ferramentas",
    # }
    single_news = {
        "url": url,
        #  Os textos coletados em title e summary podem conter alguns
        # caracteres vazios ao final. O teste espera que esses caracteres
        # sejam removidos.
        "title": title.strip(),
        "timestamp": timestamp,
        "writer": writer,
        #  Muita atenção aos tipos dos campos, por exemplo, category é uma
        # string enquanto reading_time é numérico.
        "reading_time": reading_time_int,
        #  Os textos coletados em title e summary podem conter alguns
        # caracteres vazios ao final. O teste espera que esses caracteres
        # sejam removidos e também aguarda uma string unica caso receba uma
        # lista de string/paragrafos, como usei getall e montei essa lista[0]
        # posso usar join e concatenar numa unica string
        "summary": "".join(summary).strip(),
        "category": category,
    }
    print(f"\numa unica noticia:\n{single_news}")

    return single_news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
