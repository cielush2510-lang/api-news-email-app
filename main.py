import numbers

import requests

api_key = "a6d100d9335646c4995a8d5199be75da"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2026-07-03&sortBy=publishedAt&apiKey="
       "a6d100d9335646c4995a8d5199be75da")

request = requests.get(url)
content = request.json()
print(content["articles"][0])
for article in content["articles"]:
    print(article["title"] + "\n")
    print(article["description"])