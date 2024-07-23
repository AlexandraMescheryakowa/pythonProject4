import requests
from requests import Response

from src.api_vacancy_website import APIGetData


class APIHeadHunter(APIGetData):
    """ Класс для API c hh.ru """

    def __init__(self) -> object:
        """ Инициация класса - ввод параметров подключения к сайту вакансий hh.ru"""
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "per_page": "", "only_with_salary": True}

    def get_response(self, keyword, per_page) -> Response:
        """ Отправить запрос на сайт """
        self.params["text"] = keyword
        self.params["per_page"] = per_page
        try:
            return requests.get(self.url, params=self.params)
        except:
            raise 'Не удалось прочитать данные с сайта'

    def get_data(self, keyword: str, per_page: int):
        """ Получить данные по вакансиям с сайта """
        try:
            return self.get_response(keyword, per_page).json()["items"]
        except:
            raise 'Не удалось обработать данные с сайта'

    @property
    def structure_fields(self):
        """ Получить структуру соответствия данных сайта hh.ru классу Vacancy"""

        return {'name': 'name',
                'area_name': 'area/name',
                'vacancies_url': 'url',
                'salary_currency': 'salary/currency',
                'salary_from': 'salary/from',
                'salary_to': 'salary/to',
                'requirement': 'snippet/requirement',
                'responsibility': 'snippet/responsibility',
                'employment': 'employment/name',
                'experience': 'experience/name',
                'schedule': 'schedule/name'
                }
