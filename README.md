# Final_proj_youjile

## Шаблон для автоматизации тестирования на python

### Шаги
1. Склонировать проект git clone `https://github.com/fedorovai1964/Final_proj_youjile.git`
2. Установить все зависимости
3. Запустить тесты `pytest -s -v`
4. Сгенерировать отчет `allure generate allure-files -o allure-report`
5. Открыть отчет `allure open allure-report`

### Стек:
- pytest
- selenium
- requests
- _sqlalchemy_
- allure
- config
- webdriver-manager

### Структора:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
- ./db - хелперы для работы с БД
 
### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/) 
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)

### Библиотеки
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- _pip install -r requirements.txt_
- pip install allure-pytest
- pip3 install requests
