import requests

api_key = "5a2f6ad2884b4b15b6142145ad61d28a"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2022-11-27&sortBy=publishedAt&apiKey=" \
      "5a2f6ad2884b4b15b6142145ad61d28a"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access article titles & descriptions
for article in content["articles"]:
    print(article["title"])
    