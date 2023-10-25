# Запрос погоды с сервиса [wttr.in](https://wttr.in)

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как использовать

```
from weather import request_weather
 
request_weather(place, [params])
```
Список параметров и формат местоположений смотри на сайте сервиса [wttr.in](https://wttr.in/:help)

 ### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
