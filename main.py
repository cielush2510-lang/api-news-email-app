import requests
from send_email import send_email

topic = "politics"
api_key = "a6d100d9335646c4995a8d5199be75da"
url = (f"https://newsapi.org/v2/everything?q={topic}&"
       f"from=2026-07-03&sortBy=popularity&"
       f"apiKey={api_key}")

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = f"Subject: Daily {topic.title()} News\n\n" + body
body = body.encode("utf-8")
send_email(body)