# Agile Projects

Agile Projects — это приложение для управления проектами на основе Django, которое позволяет пользователям управлять проектами, задачами и пользователями. Этот README содержит обзор проекта, инструкции по установке, настройке и запуску тестов.

## Содержание

- [Обзор проекта](#обзор-проекта)
- [Установка](#установка)
- [Конфигурация](#конфигурация)
- [Запуск тестов](#запуск-тестов)
- [API эндпоинты](#api-эндпоинты)
- [Вклад в проект](#вклад-в-проект)
- [Лицензия](#лицензия)

## Обзор проекта

Agile Projects разработано для помощи командам в управлении своими проектами и задачами в гибкой манере. Приложение включает функции для управления пользователями, создания проектов и отслеживания задач.

## Установка

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/yourusername/agile-projects.git
   cd agile-projects

## Создайте виртуальное окружение:

# bash
Copy code
python -m venv venv
source venv/bin/activate  # Для Linux/MacOS
venv\Scripts\activate  # Для Windows
## Установите зависимости:

bash
Copy code
pip install -r requirements.txt
## Примените миграции:

bash
Copy code
python manage.py migrate
# Создайте суперпользователя:

bash
Copy code
python manage.py createsuperuser
Запустите сервер:

bash
Copy code
python manage.py runserver
Конфигурация
Проект использует файл settings.py для конфигурации. Убедитесь, что все необходимые настройки выполнены, включая базу данных и секретный ключ Django.

## Запуск тестов
Для запуска тестов используйте следующую команду:

bash
Copy code
pytest --cache-clear apps/users/tests/test_user_api_bdd.py
API эндпоинты
UserListGenericView: Получение списка всех пользователей.

RegisterUserGenericView: Регистрация нового пользователя.

Вклад в проект
Мы приветствуем вклад в проект. Пожалуйста, следуйте нашим рекомендациям по вкладу.

Лицензия
Этот проект лицензирован под MIT License.