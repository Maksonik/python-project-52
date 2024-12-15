### Hexlet tests and linter status:
[![Actions Status](https://github.com/ShcherbinaDmitry/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ShcherbinaDmitry/python-project-52/actions)
[![lint check](https://github.com/ShcherbinaDmitry/python-project-52/actions/workflows/lint-check.yml/badge.svg)](https://github.com/ShcherbinaDmitry/python-project-52/actions/workflows/lint-check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/7a6116abd3b35320a7ff/maintainability)](https://codeclimate.com/github/ShcherbinaDmitry/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/7a6116abd3b35320a7ff/test_coverage)](https://codeclimate.com/github/ShcherbinaDmitry/python-project-52/test_coverage)



Task manager - финальный проект, разработанный в рамках обучения на курсе Хекслет. Это сайт на основе Djangо, который позволяет распределять задачи среди пользователей и следить за их выполнением.

***
## Перед установкой
Для установки и запуска проекта вам потребуется Python (версии  3.9 и выше), инструмент для управления зависимостями Poetry.

Перед началом использования проекта убедитесь, что вышеописанные утилиты установлены на вашем устройстве. В противном случае используйте официальную документацию для установки.

## Установка

1. Склонируйте репозиторий с проектом на ваше локальное устройство:
```
git clone https://github.com/ShcherbinaDmitry/python-project-52.git
```
2. Перейдите в директорию проекта:
```
cd python-project-52
```
3. Установите необходимые зависимости с помощью Poetry:
```
poetry install
```
4. Создайте файл .env, который будет содержать ваши конфиденциальные настройки:

```
cp .env.example .env
```

Откройте файл .env и ознакомьтесь с его содержимым. Замените значение ключей SECRET_KEY и DATABASE_URL.

5. Выполните команды: 
```
make migrate
```

***

## Использование
1. Для запуска сервера в продакшн среде с помощью Gunicorn выполните команду:

```
make start
```
По умолчанию сервер будет доступен по адресу http://0.0.0.0:8000.

2. Также можно запустить сервер локально в режиме разработки с активным отладчиком:

```
make dev
```
Сервер для разработки будет доступен по адресу http://127.0.0.1:5000.

3. Проект можно использовать онлайн (например с помощью стороннего сервиса [render.com](https://dashboard.render.com/)). Следуйте инструкциям с официального сайта для добавления веб-сервиса и онлайн базы данных. Не забывайте про использования переменных окружения.