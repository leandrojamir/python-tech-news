# Boas-vindas ao repositório do Tech News

<details>
  <summary><strong>👨‍💻 O que deverá ser desenvolvido</strong></summary><br />

  Você fará um projeto que tem como principal objetivo fazer consultas em notícias sobre tecnologia.

  As notícias podem ser obtidas através da raspagem do [_blog da Trybe_](https://blog.betrybe.com).

  <strong>🚵 Habilidades a serem trabalhadas:</strong>
  <ul>
    <li>Utilizar o terminal interativo do Python</li>
    <li>Escrever seus próprios módulos e importá-los em outros códigos</li>
    <li>Aplicar técnicas de raspagem de dados</li>
    <li>Extrair dados de conteúdo HTML</li>
    <li>Armazenar os dados obtidos em um banco de dados</li>
  </ul>

</details>

<details>
  <summary><strong>🧱 Estrutura do Projeto</strong></summary><br />
  Este repositório já contém um template com a estrutura de diretórios e arquivos, tanto de código quanto de teste criados. Veja abaixo:

  ```
  Legenda:
  🔸Arquivos que não podem ser alterados
  🔹Arquivos a serem alterados para realizar os requisitos.
  .
  ├── tech_news
  │   ├── analyzer
  │   │   ├── 🔹ratings.py
  │   │   ├── 🔸reading_plan.py
  │   │   └── 🔹search_engine.py
  │   ├── 🔸database.py
  │   └── 🔹menu.py
  │   └── 🔹scraper.py
  ├── tests
  │   ├── reading_plan
  │   │   ├── 🔸__init__.py
  │   │   ├── 🔸conftest.py
  │   │   ├── 🔸mocks.py
  │   │   └── 🔹test_reading_plan.py
  │   ├── 🔸assets/*
  │   ├── 🔸__init__.py
  │   ├── 🔸marker.py
  │   ├── 🔸test_menu.py
  │   ├── 🔸test_ratings.py
  │   ├── 🔸test_scraper.py
  │   └── 🔸test_search_engine.py
  ├── 🔸dev-requirements.txt
  ├── 🔸docker-compose.yml
  ├── 🔸Dockerfile
  ├── 🔸pyproject.toml
  ├── 🔸README.md
  ├── 🔸requirements.txt
  ├── 🔸setup.cfg
  ├── 🔸setup.py
  ├── 🔸trybe-filter-repo.sh
  └── 🔸trybe.yml
  ```

  Apesar do projeto já possuir uma **estrutura base**, você perceberá que possui arquivos vazios, ou seja, neles você quem deve implementar as classes. Novos arquivos e funções podem ser criados conforme a necessidade da sua implementação, porém não remova arquivos já existentes.

</details>

<details>
  <summary><strong>🎛 Linter</strong></summary><br />

  Para garantir a qualidade do código, vamos utilizar neste projeto o linter `Flake8`.
  Assim o código estará alinhado com as boas práticas de desenvolvimento, sendo mais legível
  e de fácil manutenção! Para rodá-lo localmente no projeto, execute o comandos abaixo:

  ```bash
  python3 -m flake8
  ```

  ⚠️ **PULL REQUESTS COM ISSUES DE LINTER NÃO SERÃO AVALIADAS.
  ATENTE-SE PARA RESOLVÊ-LAS ANTES DE FINALIZAR O DESENVOLVIMENTO!** ⚠️
</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

# Requisitos obrigatórios

## 1 - Crie a função `fetch`

local: `tech_news/scraper.py`

Antes de fazer scrape, precisamos de uma página! Esta função será responsável por fazer a requisição HTTP ao site e obter o conteúdo HTML.
Alguns cuidados deverão ser tomados: como a nossa função poderá ser utilizada várias vezes em sucessão, na nossa implementação devemos nos assegurar que um [Rate Limit](https://app.betrybe.com/learn/course/5e938f69-6e32-43b3-9685-c936530fd326/module/290e715d-73e3-4b2d-a3c7-4fe113474070/section/7e82ac53-a588-412b-95a5-19727d70ed3a/day/9488d307-4a72-4c82-887f-d860ad20a1af/lesson/d1b4c16d-1cef-4fdd-a7e6-a45770074077) será respeitado.

* A função deve receber uma URL
* A função deve fazer uma requisição HTTP `get` para esta URL utilizando a função `requests.get`
* A função deve retornar o conteúdo HTML da resposta.
* A função deve respeitar um Rate Limit de 1 requisição por segundo; Ou seja, caso chamada múltiplas vezes, ela deve aguardar 1 segundo entre cada requisição que fizer.
**Dica:** Uma forma simples de garantir que cada requisição seja feita com um intervalo mínimo de um segundo é utilizar `time.sleep(1)` antes de cada requisição. (Existem outras formas mais eficientes.)
* Caso a requisição seja bem sucedida com `Status Code 200: OK`, deve ser retornado seu conteúdo de texto;
* Caso a resposta tenha o código de status diferente de `200`, deve-se retornar `None`;
* Caso a requisição não receba resposta em até 3 segundos, ela deve ser abandonada (este caso é conhecido como "Timeout") e a função deve retornar None.

📌 Você vai precisar definir o _header_ `user-agent` para que a raspagem do blog da Trybe funcione corretamente. Para isso, preencha com o valor `"Fake user-agent"` conforme exemplo abaixo:

```python
{ "user-agent": "Fake user-agent" }
```

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>

  Abra um terminal Python importando estas funções através do comando:

  `python3 -i tech_news/scraper.py`

  Agora invoque as funções utilizando diferentes parâmetros.
  Exemplo:

  ```python
  html = fetch(url_da_noticia)
  scrape_news(html)
  ```

</details>

## 2 - Crie a função `scrape_updates`

local: `tech_news/scraper.py`

Para conseguirmos fazer o scrape da página de uma notícia, primeiro precisamos de links para várias páginas de notícias. Estes links estão contidos na página inicial do blog da Trybe (<https://blog.betrybe.com>).

Esta função fará o scrape da página para obter as URLs das páginas de notícias. Vamos utilizar as ferramentas que aprendemos no curso, como a biblioteca Parsel, para obter os dados que queremos de cada página.

* A função deve receber uma string com o conteúdo HTML da página inicial do blog
* A função deve fazer o scrape do conteúdo recebido para obter uma lista contendo as URLs das notícias listadas.
  * ⚠️ _Atenção:_ **NÃO** inclua a notícia em destaque da primeira página, apenas as notícias dos cards.
* A função deve retornar esta lista.
* Caso não encontre nenhuma URL de notícia, a função deve retornar uma lista vazia.

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>

  Abra um terminal Python importando estas funções através do comando:
  
  `python3 -i tech_news/scraper.py`
  
  Agora invoque as funções utilizando diferentes parâmetros. Exemplo:

  ```python
  html = fetch(url_da_noticia)
  scrape_updates(html)
  ```

</details>

## 3 - Crie a função `scrape_next_page_link`

local: `tech_news/scraper.py`

Para buscar mais notícias, precisaremos fazer a paginação, e para isto, vamos precisar do link da próxima página. Esta função será responsável por fazer o scrape deste link.

* A função deve receber como parâmetro uma `string` contendo o conteúdo HTML da página de novidades (<https://blog.betrybe.com>)
* A função deve fazer o scrape deste HTML para obter a URL da próxima página.
* A função deve retornar a URL obtida.
* Caso não encontre o link da próxima página, a função deve retornar `None`

## 4 - Crie a função `scrape_news`

local: `tech_news/scraper.py`

Agora que sabemos pegar páginas HTML, e descobrir o link de notícias, é hora de fazer o scrape dos dados que procuramos!

* A função deve receber como parâmetro o conteúdo HTML da página de uma única notícia
* A função deve, no conteúdo recebido, buscar as informações das notícias para preencher um dicionário com os seguintes atributos:
  * `url` - link para acesso da notícia.
  * `title` - título da notícia.
  * `timestamp` - data da notícia, no formato `dd/mm/AAAA`.
  * `writer` - nome da pessoa autora da notícia.
  * `reading_time` - número de minutos necessários para leitura.
  * `summary` - o primeiro parágrafo da notícia.
  * `category` - categoria da notícia.

* Exemplo de um retorno da função com uma notícia fictícia:

```json
{
  "url": "https://blog.betrybe.com/novidades/noticia-bacana",
  "title": "Notícia bacana",
  "timestamp": "04/04/2021",
  "writer": "Eu",
  "reading_time": 4,
  "summary": "Algo muito bacana aconteceu",
  "category": "Ferramentas",
}
  ```

📌 Muita atenção aos tipos dos campos, por exemplo, `category` é uma string enquanto `reading_time` é numérico.

📌 Os textos coletados em `title` e `summary` podem conter alguns caracteres vazios ao final. O teste espera que esses caracteres sejam removidos.

📌 **É bom saber que** ao fazer scraping na vida real, você está sempre "refém" de quem construiu o site. Por exemplo, pode ser que nem toda notícia tenha **exatamente** o mesmo HTML/CSS e você precise de criatividade para contornar isso.

📌 Caso uma tag possua outras tags aninhadas, você pode usar o seletor ```*``` para obter informações da tag ancestral e também de suas tags descendentes.

<details>

<summary> <strong>Veja um exemplo:</strong> </summary>

```html
<p>
  Recentemente, a Alemanha fez a
  <a
    href="https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm"
    rel="noopener noreferrer"
    target="_blank"
    >Tesla</a
  >
  “pisar no freio” quanto ao uso de termos comerciais relacionados a carros
  autônomos, mas quem pensa que esse é um sinal de resistência à introdução de
  novas tecnologias se engana. Isso porque, de acordo o
  <em>Automotive News Europe</em>, o país está se preparando para se tornar o
  primeiro do mundo a criar uma ampla estrutura para regulamentar tais
  veículos de nível 4.
</p>
```

Repare que dentro da tag _p_ encontram-se duas outras tags. Esse é um caso onde a tag _p_ é uma ancestral e as tags _a_ e _em_ são as descendentes. Assim, podemos usar o seletor ```*``` para fazer refrência à todas essas tags simultaneamente.

Você pode encontrar mais informações sobre esse seletor [aqui](https://www.w3schools.com/cssreF/css_selectors.php#:~:text=with%20id%3D%22firstname%22-,*,-*)

</details>

## 5 - Crie a função `get_tech_news` para obter as notícias

local: `tech_news/scraper.py`

Agora, chegou a hora de aplicar todas as funções que você acabou de fazer. Com estas ferramentas prontas, podemos fazer nosso scraper mais robusto com a paginação.

* A função deve receber como parâmetro um número inteiro `n` e buscar as últimas `n` notícias do site.
* Utilize as funções `fetch`, `scrape_updates`, `scrape_next_page_link` e `scrape_news` para buscar as notícias e processar seu conteúdo.
* As notícias buscadas devem ser inseridas no MongoDB; Para acessar o banco de dados, importe e utilize as funções que já temos prontas em `tech_news/database.py`
* Após inserir as notícias no banco, a função deve retornar estas mesmas notícias.

📌 De aqui em diante, usaremos o MongoDB.

Rodar MongoDB via Docker: `docker-compose up -d mongodb` no terminal.
Para mais detalhes acerca do mongo com o docker, olhe o arquivo `docker-compose.yml`

Caso queira instalar e rodar o servidor MongoDB nativo na máquina, siga as instruções no tutorial oficial:
Ubuntu: <https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/>  
MacOS:  <https://docs.mongodb.com/guides/server/install/>
  
Com o banco de dados rodando, o nosso módulo conseguirá acessá-lo sem problemas. Importe o módulo `tech_news/database.py` e chame as funções contidas nele.
Não altere as funções deste módulo; elas serão utilizadas nos testes.

## 6 - Teste a classe `ReadingPlanService`

local: `tests/reading_plan/test_reading_plan.py`

Agora que temos meios de popular nosso banco de dados com notícias, podemos fazer uso de uma funcionalidade implementada por outro time!

O serviço de **planejamento de leituras**, implementado no arquivo `tech_news/analyzer/reading_plan.py`, coleta as notícias do banco de dados e as divide em 2 agrupamentos:

1. `readable`: notícias que podem ser lidas em até `X` minutos
2. `unreadable`: notícias que **não** podem ser lidas em até `X` minutos

Além disso, as notícias `readable` são organizadas em sub-grupos cuja soma dos tempos de leitura seja menor que `X`. Assim, a pessoa leitora pode ler mais do que 1 notícia sem ultrapassar o tempo disponível!

O valor de `X`, que é o tempo de leitura que uma pessoa tem disponível, é passado por parâmetro no método `group_news_for_available_time`, que é um **método de classe**.

📌 Você deve implementar o teste `test_reading_plan_group_news` para garantir o funcionamento correto deste método que está explicado abaixo. Ah, não se preocupe em testar a chamada dos outros métodos da classe!

📌 O método `group_news_for_available_time` utiliza a função `find_news` do módulo `tech_news.database` para coletar as notícias no banco de dados. Pode ser importante mockar essa função para que o resultado do teste não dependa do banco de dados.

<details>
  <summary>
    <b>👀 Entenda o retorno do método <code>group_news_for_available_time</code> </b>
  </summary>

Um exemplo de resultado da chamada `ReadingPlanService.group_news_for_available_time(10)` pode ser:

```python
{
    "readable": [  # Grupos de notícias que tem 'reading_time' menor ou igual ao parâmetro
        {
            "unfilled_time": 3,  # tempo disponível restante (não preenchido pelas notícias escolhidas)
            "chosen_news": [  # Lista de notícias escolhidas
                (
                    "Não deixe para depois: Python é a linguagem mais quente do momento",  # 'title' da notícia
                    4,  # 'reading_time' da notícia
                ),
                (
                    "Selenium, BeautifulSoup ou Parsel? Entenda as diferenças",
                    3,
                ),
            ],
        },
        {
            "unfilled_time": 0,
            "chosen_news": [
                (
                    "Pytest + Faker: a combinação poderosa dos testes!",
                    10,
                )
            ],
        },
    ],
    "unreadable": [  # Lista de notícias que tem 'reading_time' maior que o parâmetro
        ("FastAPI e Flask: frameworks para APIs em Python", 15),
        ("A biblioteca Pandas e o sucesso da linguagem Python", 12),
    ],
}
```

</details>

## 7 - Crie a função `search_by_title`

local: `tech_news/analyzer/search_engine.py`

Além de testar funcionalidades que acessam o banco, podemos fazer as nossas próprias funcionalidades! Esta função irá fazer buscas por título.

* A função deve receber uma string com um título de notícia
* A função deve buscar as notícias do banco de dados por título
* A função deve retornar uma lista de tuplas com as notícias encontradas nesta busca.
Exemplo:

```python
[
  ("Título1_aqui", "url1_aqui"),
  ("Título2_aqui", "url2_aqui"),
  ("Título3_aqui", "url3_aqui"),
]
```

* A busca deve ser _case insensitive_

* Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.

📌 Lembre-se; para acesso ao banco de dados importe `db` definido no módulo `tech_news/database.py`.

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>
  Abra um terminal Python importando esta função através do comando
  
  `python3 -i tech_news/analyzer/search_engine.py`
  
  Agora invoque a função utilizando diferentes parâmetros. Exemplo:
  
  `search_by_title("Algoritmos")`.

</details>

## 8 - Crie a função `search_by_date`

local: `tech_news/analyzer/search_engine.py`

Esta função irá buscar as notícias do banco de dados por data.

* A função deve receber como parâmetro uma data no formato ISO `AAAA-mm-dd`
* A função deve buscar as notícias do banco de dados por data.
* A função deve ter retorno no mesmo formato do requisito anterior.
* Caso a data seja inválida, ou esteja em outro formato, uma exceção `ValueError` deve ser lançada com a mensagem `Data inválida`.
* Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.

📌 Lembre-se: A função recebe uma data no formato ISO `AAAA-mm-dd`, mas no banco a data está salva no formato `dd/mm/AAAA`. **Dica:** Lembrem-se de como trabalhamos com datas nos projetos anteriores.

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>
  Abra um terminal Python importando esta função através do comando
  
  `python3 -i tech_news/analyzer/search_engine.py`
  
  Agora invoque a função utilizando diferentes parâmetros. Exemplo:
  
  `search_by_date("2021-04-04")`

</details>

## 9 - Crie a função `search_by_category`

local: `tech_news/analyzer/search_engine.py`

Esta função irá buscar as notícias por categoria.

* A função deve receber como parâmetro o nome da categoria completo.
* A função deve buscar as notícias do banco de dados por categoria.
* A função deve ter retorno no mesmo formato do requisito anterior.
* Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.
* A busca deve ser _case insensitive_

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>
  
  Abra um terminal Python importando esta função através do comando:
  
  `python3 -i tech_news/analyzer/search_engine.py`
  
  Agora invoque a função utilizando diferentes parâmetros. Exemplo:
  
  `search_by_category("Ferramentas")`.
</details>

## 10 - Crie a função `top_5_categories`

local: `tech_news/analyzer/ratings.py`

Esta função irá listar as cinco categorias com maior ocorrência no banco de dados.

* A função deve buscar as categorias do banco de dados e calcular a sua "popularidade" com base no número de ocorrências;
* As top 5 categorias da análise devem ser retornadas em uma lista no formato `["category1", "category2"]`;
* A ordem das categorias retornadas deve ser da mais popular para a menos popular, ou seja, categorias que estão em mais notícias primeiro;
* Em caso de empate, o desempate deve ser por ordem alfabética de categoria.
* Caso haja menos de cinco categorias, no banco de dados, deve-se retornar todas as categorias existentes;
* Caso não haja categorias disponíveis, deve-se retornar uma lista vazia.

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>
  Abra um terminal Python importando esta função através do comando:
  
  `python3 -i tech_news/analyzer/ratings.py`
  
  Agora invoque a função utilizando diferentes parâmetros. Exemplo:
  
  `top_5_categories()`.

</details>

---

# Requisitos bônus

## 11 - Crie a função `analyzer_menu`

local: `tech_news/menu.py`

Esta função é o menu do nosso programa. Através dele poderemos operar as funcionalidades que criamos. Será um menu de opções, em que cada opção pede as informações necessárias para disparar uma ação.

* O texto exibido pelo menu deve ser exatamente:

```
Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair.
```

* Caso a opção `0` seja selecionada, seve-se exibir a mensagem "Digite quantas notícias serão buscadas:"
* Caso a opção `1` seja selecionada, deve-se exibir a mensagem "Digite o título:";
* Caso a opção `2` seja selecionada, deve-se exibir a mensagem "Digite a data no formato aaaa-mm-dd:";
* Caso a opção `3` seja selecionada, deve-se exibir a mensagem "Digite a categoria:";
* Caso a opção não exista, exiba a mensagem de erro "Opção inválida" na `stderr`.

📌 A função `input` deve ser utilizada para receber a entrada de dados da pessoa usuária.

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>
  
  Dentro de um ambiente virtual onde seu projeto foi configurado, para o menu ser exibido digite o comando
  
  `tech-news-analyzer`
  
  Isto acontece pois durante a configuração inicial do projeto já configuramos para que a função seja corretamente chamada quando este comando seja invocado.
</details>

## 12 - Implemente as funcionalidades do menu

local: `tech_news/menu.py`

* Quando selecionada uma opção do menu, e inseridas as informações necessárias, a ação adequada deve ser realizada.
* Caso a opção `0` seja selecionada, a função `get_tech_news` deve ser importada;
* Caso a opção `1` seja selecionada, a função `search_by_title` deve ser importada e seu resultado deve ser impresso em tela;
* Caso a opção `2` seja selecionada, a função `search_by_date` deve ser importada e seu resultado deve ser impresso em tela;
* Caso a opção `3` seja selecionada, a função `search_by_category` deve ser importada e seu resultado deve ser impresso em tela;
* Caso a opção `4` seja selecionada, a função `top_5_categories` deve ser importada e seu resultado deve ser impresso em tela;
* Caso a opção `5` seja selecionada, deve-se encerrar a execução do script e exibir a mensagem "Encerrando script";
* Caso alguma exceção seja lançada, a mesma deve ser capturada e sua mensagem deve ser exibida na saída padrão de erros (`stderr`).

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>
  
  Dentro de um ambiente virtual onde seu projeto foi configurado, para interagir com o menu digite o comando
  
  `tech-news-analyzer`
</details>
