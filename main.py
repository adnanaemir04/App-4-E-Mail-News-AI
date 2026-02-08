import requests

from CurrentSourceCode.main import article
from send_email import send_email

topic = "tesla"
api_key = "6613926791cd4d57a94d7d99d0909e3b"
url = "https://newsapi.org/v2/everything?" \
       f"q={topic}&" \
       "sortBy=publishedAt&" \
        "apiKey=6613926791cd4d57a94d7d99d0909e3b&" \
        "language=en"

#Make request
request = requests.get(url)

#Get dictionary with data
content = request.json()

#access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        body = "Subject:Today's News" + "\n"  \
                + body + article["title"] + "\n" \
                + article["description"] + "\n" \
                + article["url"] + 2*"\n"

body = body.encode("UTF-8")
send_email(message=body)
