# Truks load app
Решение тестовой задачи.
Необходимо было сделать Django приложение, которое отображает таблицу 
со справочными параметрами самосвалов и текущее значение перегруза.

# Зависимости
Для запуска необходимо установить django ```pip install django```, или
перейти в папку с проектом в терменале и ввести:
```bash
$ pipenv install
```

# Запуск
После установки зависимостей в консоли необхоимо набрать
```bash
$ python manage.py runserver
```
# Добавление техники
Запускаем приложение, переходим по адресу 'localhost:8000/admin', 
логин amdin пароль 123 и добавляем необходимую технику.

# P.S.
Данное приложение не предназначенно к использованию в боевых условиях и в большей мере нуждается в дороботках.
Данное приложение использует встроенный тестовый сервер.
В конфиге для облегчения цикла прототипирования были закоментированны AUTH_PASSWORD_VALIDATORS, 
что является грубым нарушение безопасности.
В данном приложении используается в качестве базы данных sqlite, которую так-же необходимо заменить 
для использования в боевых условиях. 
