import openFoodFactsPull
import requests

r = requests.get("http://127.0.0.1:8000/item/", headers = {"Content-Type":"text"})