## Тестовое задание для проверки функциональности добавления объявления в избранное. 

## Требования к ПО:
- Python 3.11+ - [www.python.org/getit/](https://www.python.org/getit/)
- Виртуальное окружение (будет в инструкции ниже)
- Selenium (будет в инструкции ниже)
- Google Chrome (тест для одного браузера) [скачать](https://www.google.com/intl/ru_ru/chrome/) можно тут
- ChromeDriver [скачать](https://sites.google.com/chromium.org/driver/) можно тут

## Как запустить тест (командная строка Windows): 
- Создать папку, в которой будет храниться виртуальное окружение и переходим в неё
```
mkdir environment

cd environment
```
- Создать вируальное окружение:
```
python -m venv selenium_env
```
- Активировать виртуальное окружение
```
selenium_env\Scripts\activate.bat
```
- Установить Selenium
```
pip install selenium==4.*
```
- Копировать репозиторий
```
git clone https://github.com/alex383rynda/avito_favorites_test
```
- Перейти в папку с тестом и запустить его
```
cd avito_favorites_test

python add_item_to_favorites_test.py
```

## Описание работы теста
После запуска теста, открывается браузер в режиме инкогнито (чтобы провести тест для неавторизованного пользователя), после чего объявление добавляется в избранное (находясь на странице объявления).

Перед переходом в раздел "Избранное" происходит проверка по элементу ![Здесь была картинка](https://github.com/alex383rynda/avito_favorites_test/blob/main/sample_image.png) на странице объявления (ждём пока пока айтем не добавится).


После проверки элемента будет выполнен переход в раздел "Избранное". Здесь будет происходить поиск названия объявления, которое было взято со страницы добавляемого объявления. Если название объявления не будет найдено, то тест завершится с ошибкой:
```
Айтем не добавился в избранное(на странице избранных айтемов)
```
Если название будет найдено, тест завершится без ошибки:
```
Объявление успешно добавлено в избранные
```
