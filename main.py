import requests

api_key = "6613926791cd4d57a94d7d99d0909e3b"
url = "https://newsapi.org/v2/everything?q=tesla&" \
       "sortBy=publishedAt&apiKey=6613926791cd4d57a94d7d99d0909e3b"

#Make request
request = requests.get(url)

#Get dictionary with data
content = request.json()

#access the article titles and description
for article in content["articles"]:
    print(article['title'])
    print(article['description'])