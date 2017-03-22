Simple Flask App
================

Aplikacja wyświetlająca imię i wiadomość w różnych formatach.

- Rozpocząnając pracę z projektem:

  ::

    mkvirtualenv wsb-simple-flask-app
    pip install -r requirements.txt
    pip install -r test_requirements

- Kontynuując pracę z projektem:

  ::

    workon wsb-simple-flask-app

- Uruchamianie applikacji:

  :: 

    python main.py

    # albo:
    PYTHONPATH=. FLASK_APP=hello_world flask run

- Uruchamianie testów:

  ::

    ...

- Integracja z TravisCI:

  ::

    ...


Materiały
=========

- https://virtualenvwrapper.readthedocs.io/en/latest/