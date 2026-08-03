import requests
from send_email import send_email

topic = "politics"
api_key = "a6d100d9335646c4995a8d5199be75da"
url = (f"https://newsapi.org/v2/everything?"
       f"q={topic}&"
       f"from=2026-07-03&"
       f"sortBy=popularity&"
       f"apiKey={api_key}&"
       f"language=en")

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"

body = f"Subject: Daily {topic.title()} News\n\n" + body
body = body.encode("utf-8")
send_email(body)