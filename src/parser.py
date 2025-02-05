from src.vacancy import Vacancy


def parser_data_website(vacancies_from_site: dict, structure_fields) -> list:
    """ Прочитать данные с сайта в приемник """

    vacancies = []

    # распарсим записи с сайта в формат приемника
    for vacancy_from_site in vacancies_from_site:
        # запишем в словарь по ключам класса Vacancy на основе соответствии, определенной в структуре класса api
        dict_vacancies = get_dict_value(vacancy_from_site, structure_fields)

        # возвращаем отсортированный список экземпляров класса Vacancy
        # for vacancy in dict_vacancies:
        vacancies.append(Vacancy.new_vacancy(dict_vacancies))

        # отсортируем вакансии по зарплате от
        sorted(vacancies, reverse=True)

    return vacancies, dict_vacancies


def parse_string(item, key):
    """ Разбирает ключ из структуры и возвращает конечное значение по конечному пути"""

    if type(item) is not dict:
        return item

    delimiter_position = key.find('/')
    if delimiter_position == -1:
        return get_value(item, key)

    else:
        return parse_string(get_value(item, key[:delimiter_position]), key[delimiter_position + 1:])


def get_value(item, key):
    """ Возвращает из словаря значение по ключу
    item - словарь
    key - ключ
    """

    if item.get(key) is not None:
        return item[key]
    else:
        return ''


def get_dict_value(item: dict, structure: dict) -> dict:
    """ Возвращает словарь значений вакансий"""

    result = {}

    for key_container, key_file in structure.items():
        result[key_container] = parse_string(item, key_file)

    return result
