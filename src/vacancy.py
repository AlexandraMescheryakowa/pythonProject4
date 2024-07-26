from settings import COURSE_CURRENCY_EUR, COURSE_CURRENCY_USD


class Vacancy:
    """ Класс для работы с вакансиями """
    __slots__ = (
        "name",
        "area_name",
        "vacancies_url",
        "salary_from",
        "salary_to",
        "salary_from_rub",
        "salary_to_rub",
        "salary_currency",
        "requirement",
        "responsibility",
        "employment",
        "schedule",
        "experience"
    )

    def __init__(self, name, area_name, vacancies_url, salary_currency, salary_from, salary_to,
                 requirement, responsibility, employment, schedule, experience):

        self.name = name
        self.area_name = area_name
        self.vacancies_url = vacancies_url

        self.requirement = requirement
        self.responsibility = responsibility
        self.employment = employment
        self.schedule = schedule
        self.experience = experience

        self.salary_from = int(salary_from) if salary_from else 0
        self.salary_to = int(salary_to) if salary_to else 0
        self.salary_currency = salary_currency if salary_currency else 'RUR'
        self.salary_rub()

    def __str__(self):
        return (f'Вакансия: {self.name}\n'
                f'Зарплата (руб.): от {self.salary_from_rub} до {self.salary_to_rub}\n'
                f'Место работы: {self.area_name}\n'
                f'Обязанности: {self.responsibility}\n'
                f'Требования: {self.requirement}\n'
                f'Режим работы: {self.employment}\n'
                f'График работы: {self.schedule}\n'
                f'Опыт работы: {self.experience}\n'
                f'Ссылка на вакансию: <{self.vacancies_url}>\n')

    @classmethod
    def new_vacancy(cls, vacancy_data: dict):
        """ Метод возвращает экземпляр класса из словаря """

        try:
            return cls(vacancy_data['name'],
                       vacancy_data['area_name'],
                       vacancy_data['vacancies_url'],
                       vacancy_data['salary_currency'],
                       vacancy_data['salary_from'],
                       vacancy_data['salary_to'],
                       vacancy_data['requirement'],
                       vacancy_data['responsibility'],
                       vacancy_data['employment'],
                       vacancy_data['schedule'],
                       vacancy_data['experience']
                       )

        except KeyError as err:
            raise f"Ошибка чтения данных: {err}"

    def __lt__(self, other):
        """ Сравнить вакансий по зарплате"""
        if isinstance(other, self.__class__):
            return self.salary_from_rub < other.salary_from_rub
        raise 'Сравнение возможно только для экземпляров класса Vacancy'

    def salary_rub(self):
        """ Пересчитать зарплату в рубли"""

        course = 1
        # зарплату переводим в рубли, курсы для зарплаты в валюте зафиксированы в константах для USD и EUR
        if self.salary_currency == 'USD':
            course = COURSE_CURRENCY_USD
        elif self.salary_currency == 'EUR':
            course = COURSE_CURRENCY_EUR

        self.salary_from_rub = int(self.salary_from) * course
        self.salary_to_rub = int(self.salary_to * course)
