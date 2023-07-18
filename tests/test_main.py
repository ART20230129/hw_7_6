from unittest import TestCase
from main import city_search, unique_number, chanell_max, creating_folder

class cityTestCase(TestCase):
 # проверка наличия российского города в списке
    def test_city(self):
        geo = [
             {'visit1': ['Москва', 'Россия']},
             {'visit2': ['Дели', 'Индия']},
             {'visit4': ['Лиссабон', 'Португалия']},
             {'visit6': ['Лиссабон', 'Португалия']},
             {'visit8': ['Тула', 'Россия']},
             {'visit9': ['Курск', 'Россия']},
             {'visit10': ['Архангельск', 'Россия']}
             ]
        res = city_search(geo)
        city_user = "Москва"
        self.assertIn(city_user, res)

# проверка правильности координат
    def test_unique(self):

        idss = {'user1': [3, 3, 3, 15, 3],
                'user2': [1, 2, 1, 1, 1],
                 'user3': [0, 0, 0, 35]}
        res = unique_number(idss)
        self.assertGreater(res, 0)

#pytest

def test_search_chanell():
    stats_user = {'A': 550, 'B': 0, 'C': 0, 'D': 99, 'E': 1, 'F': 0}
    res = chanell_max(stats_user)
    res_2 = stats_user[res]
    expected = 550
    assert res_2 == expected

def test_yandex():
    res = creating_folder('september')
    status_code = 401
    assert res == status_code

