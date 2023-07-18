import requests
# 1. Дан список с визитами по городам и странам. Напишите код,
# который возвращает отфильтрованный список geo_logs, содержащий только визиты из России.

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

def city_search(geo):
    city_city = []
    for visit in geo_logs:
        for country in visit.values():
            if country[1] == "Россия":
                city_city.append(country[0])
    return city_city

# Выведите на экран все уникальные гео-ID из значений словаря ids.
# Т.е. список вида [213, 15, 54, 119, 98, 35]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def unique_number(ids):
    val = list(ids.values())
    unique = []
    for number in val:
        for dubl in number:
            if dubl not in unique:
                unique.append(dubl)
    return sum(unique)

# Дана статистика рекламных каналов по объемам продаж.
# Напишите скрипт, который возвращает название канала с максимальным объемом

stats = {'facebook': 155, 'yandex': 225, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

def chanell_max(statss):
    maximum = max(list(statss.values()))
    for title_channel in statss.keys():
        if statss[title_channel] == maximum:
            return title_channel

##создание папки на ЯндексДиске
def creating_folder(path):
    ''' Создание папки на Яндекс.Диске '''
    token = 'токен'
    upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
    params = {"path": path}
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
    response = requests.put(url=upload_url, headers=headers, params=params)
    return response.status_code



if __name__ == '__main__':
    result = city_search(geo_logs)
    print(result)
    result_2 = unique_number(ids)
    print(result_2)
    result_3 = chanell_max(stats)
    print(result_3)
    result_4 = creating_folder("hello")
    print(result_4)





