[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)

# **api_yatube.**
REST API для социальной сети Yatube. Через этот интерфейс смогут работать мобильное приложение или чат-бот; 
через него же можно будет передавать данные в любое приложение или на фронтенд.

## Описание задачи:
В данном проекте "api_yatube" присутствует приложение "posts" с описанием моделей Yatube. Вам необходимо реализовать API для всех моделей данного приложения.

1. Добавьте новое приложение с именем "api" и реализуйте всю необходимую логику в нем.

2. Доступ к API должен быть предоставлен только аутентифицированным пользователям. Для аутентификации используйте токены (`TokenAuthentication`).

3. Аутентифицированные пользователи могут изменять и удалять только свой контент, в то время как доступ к контенту других пользователей должен быть предоставлен только для чтения. При попытке изменить чужие данные API должно возвращать код ответа 403 Forbidden.

#### Для взаимодействия с ресурсами опишите и настройте такие эндпоинты:
1. `api/v1/api-token-auth/ (POST)`: Передайте логин и пароль, чтобы получить токен.

2. `api/v1/posts/ (GET, POST)`: Получите список всех постов или создайте новый пост.

3. `api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE)`: Получите, отредактируйте или удалите пост по его уникальному идентификатору (post_id).

4. `api/v1/groups/ (GET)`: Получите список всех групп.

5. `api/v1/groups/{group_id}/ (GET)`: Получите информацию о группе по ее уникальному идентификатору (group_id).

6. `api/v1/posts/{post_id}/comments/ (GET, POST)`: Получите список всех комментариев для поста с id=post_id или создайте новый комментарий, указав id поста, который хотите прокомментировать.

7. `api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE)`: Получите, отредактируйте или удалите комментарий по его уникальному идентификатору (comment_id) для поста с id=post_id.

## Приветствуется:
- Аккуратный код
- Соблюдение PEP8 (Pycodestyle)

### **Стек:**
![python version](https://img.shields.io/badge/Python-3.11-brightgreen)   ![django version](https://img.shields.io/badge/Django-4.2.3-brightgreen)
[![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-3.14.0-brightgreen)](https://www.django-rest-framework.org/)


### **Дополнительные библиотеки:**

![Pillow version](https://img.shields.io/badge/Pillow-10.0.0-blue) 


### **Запуск проекта в dev-режиме**
Инструкция ориентирована на операционную систему Windows и утилиту git bash.<br/>
#### Для прочих инструментов используйте аналоги команд для вашего окружения.

1. Клонируйте репозиторий и перейдите в него в командной строке:

```python
git clone https://github.com/artyom-vah/api_yatube.git
```

2. Установите и активируйте виртуальное окружение
```python
python -m venv venv
```

```python
source venv/Scripts/activate
```
* _или сразу так:_
```python
python -m venv venv && . venv/Scripts/activate
```
3. Обновите pip 
```python
python -m pip install --upgrade pip
```
4. Установите зависимости из файла requirements.txt
```python
pip install -r requirements.txt
```
5. Перейдите в папку yatube_api/
```python
cd yatube_api/
```
6. В папке с файлом manage.py создайте и выполните миграции:
```python
python manage.py makemigrations
```
```python
python manage.py migrate
```

7. Создайте суперюзера 'укажите имя пользователя, адрес электронной почты (необязательно), и Password'
```python
python manage.py createsuperuser
```

8. Запустите сервер
```python
python manage.py runserver
```
**Автор проекта: Артем Вахрушев.**