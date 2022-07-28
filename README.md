# api_final_yatube
REST_API  для социальной сети блогеров. Написан в рамках учебного курса Яндекс Практикума.

Проект позволяет управлять постами, комментариями, подписками и группами.

### Технологии
- Библиотека Django REST Framework
- Аутендификация по JWT токену

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/cortin34/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Примеры запросов/ответов API

Получить список всех постов:
```
/api/v1/posts/
```
Пример ответа:
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
Получение всех комментариев поста:
```
/api/v1/posts/{post_id}/comments/
```
Пример ответа:
```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```
Получение списка сообществ (groups)
```
/api/v1/groups/
```
Пример ответа:
```
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
```
Получение всех подписок пользователя, сделавшего запрос.
```
/api/v1/follow/
```
Пример ответа:
```
[
  {
    "user": "string",
    "following": "string"
  }
]
```


