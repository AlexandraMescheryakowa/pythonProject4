def test_write_data(json_file):
    """ Тест записи в файл """
    json_file.save_data(
        [
            {
                'name': 'Менеджер по работе с клиентами',
                'area_name': "Воронеж",
                'salary_from': 350,
                'salary_from_to': 450
            }
        ]
    )


def test_get_data(json_file):
    """ Тест чтения данных из файла  """
    result = json_file.get_data()

    # проверка количества записей результата чтения файла и его тип данных
    assert type(result) is list

    # проверка количества записей первого элемента и его тип данных
    assert (len(result[0])) == 4
    assert type(result[0]) is dict


def test_del_data(json_file):
    """ Тест удаления данных - возвращает пустой словарь """
    json_file.delete_data()
    assert json_file.get_data() == []
