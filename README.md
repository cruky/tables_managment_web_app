# tables_managment_web_app

Aplikacja internetowa pozwalająca na import danych w formacie *.CSV
Dane są później ładowane do relacyjnej bazy danych.
Przed załadowaniem następuje walidowanie danych i sprwadzenie zgodności
struktury z tą istniejącą w bazie danych. W przypadku niezgodności użytkownik jest informowany o błedach.
Aplikacja przechowuje metadane związane z tym kto i kiedy ładował dane do systemu.
Na podstawie odpowiednich filtrów użytkownicy są w stanie wyświetlać dane w formie
tabelarycznej w przeglądarce. Aplikacja wykorzystuje uwierzytelnianie.


### Features

* Read CSV
* Transform data using pandas
* Load data to PostgreSQL
* Read data from PostgreSQL
* Filter data
* Convert data to table and render HTML templates with Jinja

### Documentation

* [Architecture overview](https://github.com/cruky/tables_managment_web_app/docs/architecture)

### Resources

* HTTP: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview>
* Flask doc: <https://flask.palletsprojects.com/en/1.1.x/>
* Flask summary: <https://devopedia.org/flask>
* Pandas: <https://pandas.pydata.org/docs/reference/index.html>
* Postgresql: <https://www.postgresql.org/docs/9.6/>
* Jija: <https://jinja.palletsprojects.com/en/2.11.x/>
* Psycopg: <https://www.psycopg.org/docs/>

### License

* Free software: BSD license