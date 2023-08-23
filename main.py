import json
import requests
from flask import Flask, render_template, request, url_for, redirect
from functions import *


# api = requests.get('https://api.spoonacular.com/food/wine/dishes?wine=verdicchio&apiKey=358023a4e8234adb908c38e4bb7a13b2')
# dane = api.json()
# print(dane)
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    wines = loading_files('tekst/type_of_wines.txt')

    list = request.form.get("lista")
    if list:
        if list == "white_wine":
            type_of_wine = loading_files('tekst/white_wine.txt')



    list2 = request.form.get("lista2")
    list3 = request.form.get("lista3")

    # x2 = lista(list,list2)[0]
    # x3 = lista(list2,list3)[1]



    print(f'@@@{list}')

    context = {"wino": wines,
               "wino2": type_of_wine

               }

    return render_template("index.html", context=context)
