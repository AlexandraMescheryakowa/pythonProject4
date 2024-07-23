def test_vacancy_init(vacancy):
    """ Тесты конструктора класса """

    assert vacancy.name == "Менеджер по работе с клиентами"
    assert vacancy.area_name == 'Воронеж'
    assert vacancy.vacancies_url == "https://hh.ru/vacancy/101709979"
    assert vacancy.salary_from == 4_000_000
    assert vacancy.salary_to == 7_000_000
    assert vacancy.requirement == "Опыт работы в продажах обязателен"
    assert vacancy.responsibility == "Консультирование клиентов"
    assert vacancy.employment == 'Полная занятость'
    assert vacancy.schedule == 'Полный день'
    assert vacancy.experience == 'От 1 года до 3 лет'


def test_vacancy_str(vacancy):
    """ Проверка строкового представления вакансии """

    assert str(vacancy) == ("Вакансия: Менеджер по работе с клиентами\n"
                            "Зарплата (руб.): от 4000000 до 7000000\n"
                            "Место работы: Воронеж\n"
                            "Обязанности: Консультирование клиентов\n"
                            "Требования: Опыт работы в продажах обязателен\n"
                            "Режим работы: Полная занятость\n"
                            "График работы: Полный день\n"
                            "Опыт работы: От 1 года до 3 лет\n"
                            "Ссылка на вакансию: <https://hh.ru/vacancy/101709979>\n")


def test_vacancy_lt(vacancy, vacancy2):
    """ Проверка сравнения вакансий по зарплате """

    assert vacancy2 < vacancy
    if vacancy > vacancy2:
        assert ValueError


def test_salary_rub(vacancy2):
    """ Тест утверждает, что метод вернет вакансию в виде словаря """

    assert vacancy2.salary_from == 350
    assert vacancy2.salary_to == 450
    assert vacancy2.salary_from_rub == 35000
    assert vacancy2.salary_to_rub == 45000
