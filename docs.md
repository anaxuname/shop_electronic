Для того чтобы начать работать с приложением, необходимо скачать и установить его с помощью команды: git clone https://github.com/anaxuname/shop_electronic
Далее запустить виртуальное окружение командами:
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1 # для Windows
```
Далее необходимо в командной строке перейти в терминал и выполнить команду: `pip install -r requirements.txt`
После установки зависимостей, а также заполнения необходимых для работы програмы данных для  env-файла (пример для заполнения находится в
файле `.env_example`), необходимо в командной строке выполнить команду: `python .\manage.py runserver`
