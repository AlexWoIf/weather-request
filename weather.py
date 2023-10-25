import requests

DEFAULT_PARAMS = {'nTqMm': '', 'lang': 'ru', }


def request_weather(place, params=DEFAULT_PARAMS):
    url = f'https://wttr.in/{place}'
    response = requests.get(url, params)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    places = ['Лондон', 'Шереметьево', 'Череповец']
    for place in places:
        print(request_weather(place))
