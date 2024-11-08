# Тестовое задание

## Описание задачи

Создать тестовое приложение, которое проверит работу API.

### Требования к тестовому приложению:

1. **Среда разработки**: Любой язык и фреймворк для тестирования REST API на ваш выбор.

2. **Детали API**:
   - **POST**:
     - **Вход**: параметр `palindrome` (тип `bool`), где:
       - `True` — запрос на генерацию строки-палиндрома.
       - `False` — запрос на генерацию случайной строки, не являющейся палиндромом.
     - **Ответ**: JSON со следующей структурой:
       - `id` (UUID)
       - `result`: `str`

   - **GET**:
     - **Вход**: `id` (UUID)
     - **Ответ**: JSON с полем `result`

3. **Результат работы**: Создайте публичный репозиторий на GitHub, содержащий тестовое приложение и сопроводительную документацию.


## Сопроводительная документация

### Локальная работа с проектом
Для локального запуска приложения необходимо выполнить следующие шаги:
- Установить Python 3.11
- Установить Poetry
- Установить зависимости проекта для лакальной разработки
```bash
poetry install --sync
```

Для работы с зависимостями используется poetry и команда `make sync`, которая следит за обновлением зависимостей в файле pyproject.toml и requirements.txt

Для запуска форматеров и линтера команда `make lint`

Если необходимо вести разработку и дебаг без виртуального окружения можно использовать docker compose в качестве удаленного интерпритатора.

### Запуск тестов через докер
Для запуска тестов аналогично CI можно использовать команду
```bash
make run_api_tests
```