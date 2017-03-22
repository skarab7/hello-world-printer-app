from hello_world import app
from formater import get_formatted
from formater import SUPPORTED
from flask import request

moje_imie = "Wojtek"
msg = "Hello World!"

@app.route('/')
def index():
    output = str(request.args.get('output'))
    return get_formatted(msg, moje_imie,
                         output.lower())

@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)
