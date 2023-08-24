import json
import requests


def loading_files(file):
    date = []
    with open(file, "r") as f:
        for idx in f:
            date.append(idx)
    return date

def get_api(ask):
    api = requests.get(f'https://api.spoonacular.com/food/wine/dishes?wine={ask}&apiKey=358023a4e8234adb908c38e4bb7a13b2')
    date = api.json()
    # print(date)
    return date
