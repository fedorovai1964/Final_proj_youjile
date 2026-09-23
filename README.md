# Final_proj_youjile

## Шаблон для автоматизации тестирования на python
Система управления проектами: ru.yougile.com
Документация API: ru.yougile.com/api-v2
### Шаги
1. Склонировать проект git clone `https://github.com/fedorovai1964/Final_proj_youjile.git`
2. Установить все зависимости
3. Запустить тесты `pytest -s -v` `pip freeze > requirements.txt`
4. Сгенерировать отчет `allure generate allure-files -o allure-report`
5. Открыть отчет `allure open allure-report`

### Стек:
- pytest
- selenium
- requests
- _sqlalchemy_
- allure
- config
- configparser
- webdriver-manager
- json

### Структора:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
- ./db - хелперы для работы с БД
- ./configuration - провайдер настроек
- test_config.ini - настройки для тестов
- ./testdata провайдер тестовых данных
- test_data.json
 
### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/) 
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)
