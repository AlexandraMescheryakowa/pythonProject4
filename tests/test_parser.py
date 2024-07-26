from src.api_hh import APIHeadHunter
from src.parser import get_dict_value, parse_string


def test_parse_string(dict_from_site):
    """ Проверить разбор пути к данным по конечному пути """
    assert parse_string(dict_from_site, 'area/name') == 'Воронеж'
    assert parse_string(dict_from_site, 'salary/currency') == 'RUR'
    assert parse_string(dict_from_site, 'salary/to') == '450000'
    assert parse_string(dict_from_site, 'no_key') == ''


def test_get_dict_value(dict_from_site, structure_fields, dict_from_site_result):
    """ Проверить чтение словаря с сайта в словарь для класса Vacancy"""
    result = get_dict_value(dict_from_site, structure_fields)
    assert get_dict_value(dict_from_site, structure_fields) == dict_from_site_result


def test_structure(structure_fields):
    """ Проверка струтуры соответствия полей данных сайт hh.ru и класса Vacancy"""
    assert structure_fields == APIHeadHunter().structure_fields
