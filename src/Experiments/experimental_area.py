import functools
from pprint import pprint

import requests

from src.decorators import print_decorator


@print_decorator
def test_send_get():
    # api_url = "http://localhost:80/cereal"
    api_url = "http://localhost:80/cereal?fat[ne]=1&calories[lt]=100&calories[gt]=10&shelf=1"
    # api_url = "http://localhost:80/cereal?name[leq]=bran"

    response = requests.get(api_url)
    response_data = response.json()

    status_code = response.status_code

    print(status_code)
    pprint(response_data)


@print_decorator
def test_send_post():
    api_url = "http://localhost:80/cereal"

    values = {
        'name': 'test name',
        'mfr': 'A',
        'type': 'B',
        'calories': 100,
        'protein': 100,
        'fat': 100,
        'sodium': 100,
        'fiber': 100,
        'carbo': 100,
        'sugars': 100,
        'potass': 100,
        'vitamins': 100,
        'shelf': 100,
        'weight': 100,
        'cups': 100,
        'rating': 100
    }

    response = requests.post(api_url, json=values, auth=('hebo_user', 'test123'))
    # response = requests.post(api_url, json=values)
    response_data = response.json()

    status_code = response.status_code

    print(status_code)
    print(response_data)


@print_decorator
def test_send_update():
    api_url = "http://localhost:80/cereal"

    values = {
        'id': 79,
        'name': 'other test name',
        'mfr': 'C',
        'type': 'C',
        'calories': 100000,
        'protein': 100,
        'fat': 100,
        'sodium': 100,
        'fiber': 100,
        'carbo': 100,
        'sugars': 100,
        'potass': 100,
        'vitamins': 100,
        'shelf': 100,
        'weight': 100,
        'cups': 100,
        'rating': 1000000
    }

    response = requests.post(api_url, json=values, auth=('hebo_user', 'test123'))
    response_data = response.json()

    status_code = response.status_code

    print(status_code)
    print(response_data)


@print_decorator
def test_send_delete():
    api_url = "http://localhost:80/cereal"

    values = {"id": "78"}

    response = requests.delete(api_url, json=values, auth=('hebo_user', 'test123'))
    response_data = response.json()

    status_code = response.status_code

    print(status_code)
    print(response_data)


if __name__ == '__main__':
    # test_send_get()

    test_send_post()

    # test_send_update()
    #
    # test_send_delete()

    print('End')
