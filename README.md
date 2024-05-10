### Онлайн платформа торговой сети электроники shop_electronic

Задача:
* Создать веб-приложение с API-интерфейсом и админ-панелью.
* Создать базу данных, используя миграции Django.

Реализована модель сети по продаже электроники. Каждое звено сети ссылается только на одного поставщика оборудования (не обязательно предыдущего по иерархии) и обладает следующими элементами:
- Название;
- Контакты (email, страна, город, улица, номер дома);
- Продукты (название, модель, дата выхода продукта на рынок);
- Поставщик (предыдущий по иерархии объект сети);
- Задолженность перед поставщиком в денежном выражении с точностью до копеек;
- Время создания (заполняется автоматически при создании).

## Документация
Документация по приложению можно найти по ссылке:
https://github.com/anaxuname/shop_electronic/blob/master/docs.md

Основная конфигурация для работы приложения находится в файле `settings.py`.
Необходимо заполнить файл `.env` с данными для подключения к базе данных. Пример находится в файле `.env_example`.

В задании к приложению есть пункт "Добавить возможность фильтрации объектов по определенной стране."
Пример фильтрации по стране выглядит так:
http://127.0.0.1:8000/provider?search=Russia