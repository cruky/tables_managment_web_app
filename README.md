# tables_managment_web_app

Aplikacja internetowa pozwalająca na import danych w formacie *.CSV
Dane są później ładowane do relacyjnej bazy danych.
Przed załadowaniem następuje walidowanie danych i sprwadzenie zgodności
struktury z tą istniejącą w bazie danych. W przypadku niezgodności użytkownik jest informowany o błedach.
Aplikacja przechowuje metadane związane z tym kto i kiedy ładował dane do systemu.
Użytkownicy są w stanie wyświetlać dane w formie
tabelarycznej w przeglądarce. Aplikacja wykorzystuje uwierzytelnianie.

By zbudować aplikację należy uruchomić plik :
database_ddl/db_init.py

Nastepnie by uruchomić aplikację, należy uruchomić plik:
tables_managment_web_app/tables_managment_web_app.py

Plik CSV można znaleźć w:
tests/csv_file_test.csv

### Features

* Read CSV
* Load data to Sqlite
* Read data from Sqlite
* Convert data to table and render HTML templates with Jinja

### Technology

* Python 3.7
* pip install -r requirements.txt

### Documentation

* [Architecture overview](https://github.com/cruky/tables_managment_web_app/tree/master/docs/architecture)

### Resources

* HTTP: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview>
* Flask doc: <https://flask.palletsprojects.com/en/1.1.x/>
* Flask summary: <https://devopedia.org/flask>
* Jija: <https://jinja.palletsprojects.com/en/2.11.x/>

### License

* Free software: BSD license