# Stripe project

## Описание проекта

Проект реализует интеграцию онлайн-оплаты с помощью сервиса Stripe.

## Технологии

- Linux
- Python
- Poetry
- Django
- DRF
- PostgreSQL
- Docker
- Docker Compose
- Stripe

## Зависимости

Зависимости, необходимые для работы проекта, указаны в файле pyproject.toml.

## Как запустить проект

Для запуска проекта необходимо выполнить следующие шаги:
1. При необходимости установите Docker и Docker Compose на компьютер с помощью инструкции https://docs.docker.com/engine/install/
2. Cклонируйте репозиторий себе на компьютер
3. Создайте файл .env и заполните его, используя образец из файла .env.example
4. Соберите образ с помощью команды `docker-compose build`
5. Запустите контейнеры с помощью команды `docker-compose up`

## Файл .env.example

1. `DATABASES_NAME, DATABASES_USER, DATABASES_PASSWORD, DATABASES_HOST` - данные для подключения к БД
2. `SECRET_KEY, DEBUG, ALLOWED_HOSTS`
3. `STRIPE_SECRET_KEY, STRIPE_PUBLIC_KEY` - ключи для работы со Stripe
4. `EXCHANGE_RATE_API_KEY` - токен Apilayer

## Доступ в админку

`username=admin`

`password=admin`

## Авторы

UlianaSem

## Связь с авторами

https://github.com/UlianaSem/
