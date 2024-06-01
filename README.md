# 🗺 AppTel

[![Python Version](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![FastAPI Version](https://img.shields.io/badge/FastAPI-0.1.0-green.svg)](https://www.djangoproject.com/)
[![Docker Version](https://img.shields.io/badge/Docker-26.0-942E20.svg)](https://www.docker.com/)
[![Docker Compose Version](https://img.shields.io/badge/Docker_Compose-2.26-521E20.svg)](https://www.docker.com/)

Этот проект представляет собой Telegram-клиент на Python с использованием библиотеки Telethon.

## Возможности

- 📡 Логин клиента по QR-коду.
- ⏱ Получение новых текстовых сообщений и их сохранение, разделенное по чатам.
- 🔄 Возможность отправки текстовых сообщений другим пользователям через клиента.
- 📂 При запросе "wild: любой товар", должен запускаться парсинг wildberries с городом Москва и запросом "любой товар", бот должен отправлять 10 наименований товаров со ссылками на них.
- 📑 Возможность отправки медиа-файлов (фотографии, видео, документы).
- 📜 Развертывание приложения с использованием Docker и Docker compose


## 💽 Установка

1. Клонируйте репозиторий:

```bash
git clone git@github.com:ZuAlVi/AppTel.git
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv env

source env/bin/activate  # для Windows: env\Scripts\activate
```
3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Создайте в корне проекта файл .env и заполните его необходимыми данными взяв за пример файл .env_example


## 🚀 Запуск

1. Запустите сервер uvicorn:
```bash
uvicorn src.main:app --host 127.0.0.1 --port 8000
```

## 🔚 Эндпоинты


### POST /login
##### REQUEST

```
{
   phone: '79092991111'
}
```

#### RESPONSE

```
{
	qr_link_url: 'https://'
}
```

### GET /check/login?phone=79092991111

#### RESPONSE

```
{
	status: 'waiting_qr_login' // or logined or error
}
```

### GET /messages?phone=790929911111&uname=chat_username

#### RESPONSE

```
{
	messages: [ // last 50 messages 
		{
			username: '',
			is_self: false, //true
			message_text: ''
		}
	]
}
```


### POST /messages

#### REQUEST

```
{
	message_text: 'привет!'
	from_phone: '790929911111',
	username: 'testname'
}
```

#### RESPONSE

```
{
	status: 'ok' //error
}
```

## Документация доступна по адресу:


http://localhost:8000/docs


## 🐳 Запуск через Docker и Docker Compose

1. Docker:
    
- Создаем контейнер:

```bash
docker build . -t app-name
 ```

- Запускаем:

```bash
docker run -p 8000:8000 app-name
 ```

2. Docker Compose:

- Собираем и запускаем контейнер в фоновом режиме одной командой:

```bash
docker-compose up --build
 ```

После этого сервис будет доступен по адресу http://localhost:8000/.
