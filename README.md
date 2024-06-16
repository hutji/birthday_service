## Описание
Веб-сервис на базе Django, предоставляющий CRUD REST API
для поздравлений с днем рождения.

## Инструкции по установке
***- Клонируйте репозиторий:***
```
git clone git@github.com:hutji/birthday_service.git
```

***- Установите и активируйте виртуальное окружение:***
- для MacOS
```
python3 -m venv venv
```
- для Windows
```
python -m venv venv
source venv/bin/activate
```
 
***- Установите зависимости из файла requirements.txt:***
```
pip install -r requirements.txt
```

***- Создаем файл .env в корневой директории с содержанием .env-example:***
```
# Django settings
DJANGO_SECRET_KEY=testsecretkey
DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

# Database settings
DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432

#JWT settings
ACCESS_TOKEN_LIFETIME=604800
REFRESH_TOKEN_LIFETIME=604800
```

***- Примените миграции:***
```
python manage.py makemigrations
python manage.py migrate
```
***- Создайте суперпользователя:***
```
python manage.py createsuperuser
```
***- В папке с файлом manage.py выполните команду для локального запуска:***
```
python manage.py runserver
```
***- Локально документация доступна по адресу:***
```
http://127.0.0.1:8000/swagger/
```
***- Админка доступа по адресу:***
```
http://127.0.0.1:8000/admin/
```

## Примеры основных API эндпоинтов:
* ```login/```  POST-запрос – получение JWT токена.
 ``` json
POST
{
  "refresh": "secretkey",
  "access": "secretkey"
}
```
* ```/api/v1/employees/```  GET-запрос – получение списка сотрудников. POST-запрос – создание нового. PATCH-запрос - Изменение. Доступно с авторизацией по JWT.
 ``` json
GET
[
    {
        "id": 1,
        "user": {
            "id": 1,
            "username": "admin",
            "email": "secret@gmail.com"
        },
        "first_name": "Pavel",
        "last_name": "Lashkov",
        "date_of_birth": "1995-09-13"
    },
    {
        "id": 2,
        "user": {
            "id": 2,
            "username": "hutji",
            "email": ""
        },
        "first_name": "John",
        "last_name": "Chena",
        "date_of_birth": "2024-06-16"
    }
]


```

* ```/api/v1/users/``` GET-запрос — получение списка пользователей. POST-запрос – создание. Доступно авторизированным пользователям.
```json
GET
[
    {
        "id": 1,
        "username": "admin",
        "email": "secret@gmail.com"
    },
    {
        "id": 2,
        "username": "hutji",
        "email": ""
    }
]

```

* ```/api/v1/subscriptions/``` GET-запрос — получение списка подписок. POST-запрос – создание. Доступно авторизированным пользователям.
```json
GET
[
    {
        "id": 1,
        "subscriber": {
            "id": 1,
            "username": "admin",
            "email": "secret@gmail.com"
        },
        "employee": {
            "id": 2,
            "username": "hutji",
            "email": ""
        }
    }
]
```
## Технологии

```Backend```
* #### Django
* #### DRF
* #### Python 3.11
* #### PostgreSQL
* #### SimpleJWT
* #### Celery
* #### Redis
