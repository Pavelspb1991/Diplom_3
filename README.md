## Дипломный проект. Задание 3: тестирование UI

#### Курс по автоматизации тестирования на Python, «Яндекс Практикум»

### Структура проекта

- в папке `tests` расположены файлы с тестами
- в файле `fake_data` — функции, генерирующие рандомные тестовые данные с помощью библиотеки Faker;
- в файле `test_urls` находятся переменные с url-адресами;
- в папке `allure_results`  хранятся результаты выполнения тестов для генерации отчета;
- в файле `conftest` находятся фикстуры драйвера;
- в папке `pages` находятся файлы с методами для взаимодействия с элементами на странице;
- в папке `locators` находятся переменные с локаторами для тестов.

### Запуск автотестов

**Запуск всех тестов одной командой**

>  `pytest  --alluredir=allure_results`
