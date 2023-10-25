# -*- coding: utf-8 -*-
import requests


def request_weather(place):
    url = f'https://wttr.in/{place}?nTqMm&lang=ru'
    response = requests.get(url)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    places = ['Лондон', 'Шереметьево', 'Череповец']
    for place in places:
        print(request_weather(place))
