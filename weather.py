# -*- coding: utf-8 -*-
import requests

if __name__ == '__main__':
    places = ['Лондон', 'Шереметьево', 'Череповец']
    for place in places:
        url = f'https://wttr.in/~{place}?nTqMm&lang=ru'
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
