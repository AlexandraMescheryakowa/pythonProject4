import pytest

from settings import FILE_TEST_VACANCIES
from src.vacancy import Vacancy
from src.file_worker_json import FileWorkerJson


@pytest.fixture
def vacancy():
    return Vacancy("Менеджер по работе с клиентами",
                   "Воронеж", "https://hh.ru/vacancy/101709979",
                   "RUR", 4_000_000, 7_000_000,
                   "Опыт работы в продажах обязателен", "Консультирование клиентов",
                   "Полная занятость", "Полный день", "От 1 года до 3 лет")


@pytest.fixture()
def vacancy2():
    return Vacancy("Руководитель проектов",
                   "Россия", "https://api.hh.ru/vacancies/93353083?host=hh.ru",
                   "EUR", 350, 450,
                   "Способен работать в команде. Способен принимать решения самостоятельно.",
                   "Работать с клиентами или партнерами для решения разнообразных ситуаций. ",
                   "Стажировка", "Гибкий график", "Без опыта")


@pytest.fixture()
def json_file():
    return FileWorkerJson(filename=FILE_TEST_VACANCIES)


@pytest.fixture
def structure_fields():
    """Фикстура для структуры соответствия ключей словаря из json и класса"""
    return {'name': 'name',
            'area_name':'area/name',
            'vacancies_url':'url',
            'salary_currency':'salary/currency',
            'salary_from':'salary/from',
            'salary_to':'salary/to',
            'requirement':'snippet/requirement',
            'responsibility':'snippet/responsibility',
            'employment':'employment/name',
            'experience':'experience/name',
            'schedule':'schedule/name'
            }


@pytest.fixture()
def dict_from_site():
    return {"id": "93353083",
            "premium": 'false',
            "name": "Тестировщик комфорта квартир",
            "department": 'null',
            "has_test": 'false',
            "response_letter_required": 'false',
            "area": {"id": "26", "name": "Воронеж", "url": "https://api.hh.ru/areas/26"},
            "salary": {"from": '350000', "to": '450000', "currency": "RUR", "gross": 'false'},
            "type": {"id": "open", "name": "Открытая"},
            "address": 'null',
            "response_url": 'null',
            "sort_point_distance": 'null',
            "published_at": "2024-02-16T14:58:28+0300",
            "created_at": "2024-02-16T14:58:28+0300",
            "archived": 'false',
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=93353083",
            "branding": {"type": "CONSTRUCTOR", "tariff": "BASIC"},
            "show_logo_in_search": 'true',
            "insider_interview": 'null',
            "url": "https://api.hh.ru/vacancies/93353083?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/93353083",
            "employer": {"id": "3499705", "name": "Специализированный застройщик BM GROUP",
                         "url": "https://api.hh.ru/employers/3499705",
                         "alternate_url": "https://hh.ru/employer/3499705"},
            "snippet": {"requirement": "Опыт работы в продажах обязателен",
                        "responsibility": "Консультирование клиентов"},
            "contacts": 'null',
            "schedule": {"id": "flexible", "name": "Гибкий график"},
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "adv_response_url": 'null',
            }


@pytest.fixture
def dict_from_site_result():
    return (
        {
            'name': 'Тестировщик комфорта квартир',
            'area_name': 'Воронеж',
            'vacancies_url': 'https://api.hh.ru/vacancies/93353083?host=hh.ru',
            'salary_currency': 'RUR',
            'salary_from': '350000',
            'salary_to': '450000',
            'requirement': 'Опыт работы в продажах обязателен',
            'responsibility': 'Консультирование клиентов',
            'employment': 'Полная занятость',
            'experience': 'Нет опыта',
            'schedule': 'Гибкий график',
        }
    )


@pytest.fixture
def dict_vacancy():
    return (
        {
            'name': 'Менеджер по работе с клиентами',
            'area_name': 'Воронеж',
            'vacancies_url': 'https://hh.ru/vacancy/101709979',
            'salary_currency': 'RUR',
            'salary_from': '4_000_000',
            'salary_to': '7_000_000',
            'salary_from_rub': '4_000_000',
            'salary_to_rub': '7_000_000',
            'requirement': 'Опыт работы в продажах обязателен',
            'responsibility': 'Консультирование клиентов',
            'employment': 'Полная занятость',
            'schedule': 'Полный день',
            'experience': 'От 1 года до 3 лет',

        }
    )
