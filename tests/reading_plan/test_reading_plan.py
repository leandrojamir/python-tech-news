# 6 - Teste a classe ReadingPlanService
# local: tests/reading_plan/test_reading_plan.py
#  Agora que temos meios de popular nosso banco de dados com notícias, podemos
# fazer uso de uma funcionalidade implementada por outro time!
# Entenda o retorno do método group_news_for_available_time
# Um exemplo de resultado da chamada
#  ReadingPlanService.group_news_for_available_time(10) pode ser:
# {
#     "readable": [  #  Grupos de notícias que tem 'reading_time' menor ou
#                    # igual ao parâmetro
#         {
#             "unfilled_time": 3,  #  tempo disponível restante
#                                  # (não preenchido pelas notícias escolhidas)
#             "chosen_news": [  # Lista de notícias escolhidas
#                 (
#                     "Não deixe para depois: Python é a linguagem mais quente"
#                     " do momento",  # 'title' da notícia
#                     4,  # 'reading_time' da notícia
#                 ),
#                 (
#                     "Selenium, BeautifulSoup ou Parsel? Entenda as"
#                     " diferenças",
#                     3,
#                 ),
#             ],
#         },
#         {
#             "unfilled_time": 0,
#             "chosen_news": [
#                 (
#                     "Pytest + Faker: a combinação poderosa dos testes!",
#                     10,
#                 )
#             ],
#         },
#     ],
#     "unreadable": [  #  Lista de notícias que tem 'reading_time' maior que o
#                      # parâmetro
#         ("FastAPI e Flask: frameworks para APIs em Python", 15),
#         ("A biblioteca Pandas e o sucesso da linguagem Python", 12),
#     ],
# }
from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from unittest.mock import MagicMock, patch
import pytest
import json

with open("tests/assets/cached_news.json") as file:
    json_list = json.load(file)


#  Você deve implementar o teste test_reading_plan_group_news para garantir o
# funcionamento correto deste método que está explicado abaixo. Ah, não se
# preocupe em testar a chamada dos outros métodos da classe!
def test_reading_plan_group_news():
    mock_news = MagicMock(return_value=json_list)
    #  O serviço de planejamento de leituras, implementado no arquivo
    # tech_news/analyzer/reading_plan.py, coleta as notícias do banco de dados
    # e as divide em 2 agrupamentos:
    # readable: notícias que podem ser lidas em até X minutos
    # unreadable: notícias que não podem ser lidas em até X minutos
    #  Além disso, as notícias readable são organizadas em sub-grupos cuja
    # soma dos tempos de leitura seja menor que X. Assim, a pessoa leitora
    # pode ler mais do que 1 notícia sem ultrapassar o tempo disponível!
    with patch.object(ReadingPlanService, "_db_news_proxy", mock_news):
        #  O valor de X, que é o tempo de leitura que uma pessoa tem
        # disponível, é passado por parâmetro no método
        # group_news_for_available_time, que é um método de classe.
        result = ReadingPlanService.group_news_for_available_time(10)
        assert len(result["readable"]) == 13
        assert result["unreadable"] == [
            ("Oratória: passo a passo para falar bem e se destacar!", 15),
            ("Linguagem Lua: o que é, quais os princípios e como usar?", 12),
            ("O que é PJ: O guia completo sobre a Pessoa Jurídica!", 11),
            ("Feedback negativo: como fazer efetivamente sem criticar!", 12),
            (
                "Feedback positivo: 20 exemplos de como fazer da forma"
                " correta",
                12,
            ),
            ("Frases de liderança: As 40 mais impactantes para inspirar!", 12),
            ("Como fazer currículo para primeiro emprego?", 11),
            ("O que é software? O guia completo e fácil de aprender!", 12),
            ("Como se vestir para uma entrevista de emprego em 2022", 16),
            ("Linguagem de programação: ranking das 19 mais úteis [2023]", 26),
            ("Gatilho mental: o que é e 20 para utilizar nas vendas!", 16),
        ]

    # if available_time <= 0:
    #     raise ValueError("Valor 'available_time' deve ser maior que zero")
    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(-10)
