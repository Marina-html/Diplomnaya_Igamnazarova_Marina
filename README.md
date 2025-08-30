# Diplomnaya_Igamnazarova_Marina
Автотесты для сайта "FUN&SUN"

Проект автоматизирует тестирование сайта бронирования туров https://fstravel.com/ с помощью UI и API тестов.
Для корректной работы тестов необходимо получить токен на сайте. Нужно авторизоваться, затем открыть DevTools, Network, открыть запрос Signin, найти Cookie
В headers внести Cookie

В рамках проекта реализованы:
UI тесты ввода валидного и невалидного email при авторизации на сайте, ввода в поля "Куда" и "Откуда" корректных городов при поиске тура, минимального количества ночей при поиске тура.
API тесты запроса туров, запрос статуса аутентификации, запрос списка городов, запрос количества ночей, запрос списка отелей.
Использование Page Object для UI тестов.

 Подготовка окружения
Клонировать проект:
git clone <ссылка-на-репозиторий>
cd project

Создать виртуальное окружение и активировать его:
python -m venv venv
venv\Scripts\activate          # Windows

Установить зависимости:
pip install -r requirements.txt
 
Запуск тестов

UI тесты:
pytest test_ui.py --alluredir=allure-results

API тесты:
pytest test_api.py --alluredir=allure-results

Все тесты:
pytest --alluredir=allure-results


Просмотр Allure отчёта

Сформировать результаты:
pytest --alluredir=allure-results

Запустить сервер Allure:
allure serve allure-results

Примечания

UI тесты используют WebDriverWait вместо time.sleep() для стабильности.

API тесты используют библиотеку requests.

Проект поддерживает повторяемость тестов — можно запускать 10+ раз подряд без изменения кода.
