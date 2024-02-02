# Yatube
##### ApI для социальной сети и сеть микроблогов в который пользователи публикуют посты и могут комментировать посты других пользователей. Настроена регистрация и аутентификация пользователей, используется пагинация.

## Стэк 
- Django
- djangorestframework
- djoser


### Как запустить проект:

#### Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram_backend.git
```

```
cd api_final_yatube
```

#### Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

#### Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

#### Выполнить миграции:

```
python3 manage.py migrate
```

#### Запустить проект:

```
python3 manage.py runserver
```
#### Документация по API:

```
http://127.0.0.1:8000/redoc
```

Автор: Николай Королёв
