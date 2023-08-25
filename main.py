import json
import requests
from flask import Flask, render_template, request, url_for, redirect
from functions import *



app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():


    return render_template("index.html")


@app.route("/wine", methods=['POST', 'GET'])
def choise_wine():

    return render_template("choise_wine.html")


@app.route("/ingredients", methods=['POST', 'GET'])
def ingredients():
    ask = request.form.get('ask')
    print(ask)
    wynik = get_api_igredients(ask)
    context = {"wynik": wynik,
               }
    return render_template("igredients.html", context=context)
@app.route("/meal", methods=['POST', 'GET'])
def meal():
    ask = request.form.get('ask')
    print(ask)
    wynik = get_api_meal(ask)
    context = {"wynik": wynik,
               }

    return render_template("meal.html", context=context)

@app.route("/wine/white_wine", methods=['POST', 'GET'])
def white_wine():
    wines = loading_files('tekst/white_wine.txt')
    context = {"wino": wines,
               }
    return render_template("white_wine.html", context=context)
@app.route("/wine/white_wine/dry", methods=['POST', 'GET'])
def white_dry_wine():
    wines = loading_files('tekst/dry_white_wine.txt')
    context = {"wino": wines,
               }
    return render_template("dry_white_wine.html", context=context)

@app.route("/wine/red_wine", methods=['POST', 'GET'])
def red_wine():
    wines = loading_files('tekst/red_wine.txt')
    context = {"wino": wines,
               }
    return render_template("red_wine.html", context=context)

@app.route("/wine/red_wine/dry", methods=['POST', 'GET'])
def red_dry_wine():
    wines = loading_files('tekst/dry_red_wine.txt')
    context = {"wino": wines,
               }
    return render_template("dry_red_wine.html", context=context)

@app.route("/wine/desert_wine", methods=['POST', 'GET'])
def desert_wine():
    wines = loading_files('tekst/dessert_wine.txt')
    context = {"wino": wines,
               }
    return render_template("desert_wine.html", context=context)
@app.route("/wine/rose_wine", methods=['POST', 'GET'])
def rose_wine():
    wines = loading_files('tekst/rose_wine.txt')
    context = {"wino": wines,
               }
    return render_template("rose_wine.html", context=context)
@app.route("/wine/sparkling_wine", methods=['POST', 'GET'])
def sparkling_wine():
    wines = loading_files('tekst/sparkling_wine.txt')
    context = {"wino": wines,
               }
    return render_template("sparkling_wine.html", context=context)
@app.route("/wine/sherry_wine", methods=['POST', 'GET'])
def sherry():
    wines = loading_files('tekst/sherry.txt')
    context = {"wino": wines,
               }
    return render_template("sherry.html", context=context)
@app.route("/wine/vermouth", methods=['POST', 'GET'])
def vermouth():
    wines = loading_files('tekst/ vermouth.txt')
    context = {"wino": wines,
               }
    return render_template("vermouth.html", context=context)







