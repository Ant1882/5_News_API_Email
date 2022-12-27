import requests
from send_email import send_email

api_key = "5a2f6ad2884b4b15b6142145ad61d28a"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2022-11-27&sortBy=publishedAt&apiKey=" \
      "5a2f6ad2884b4b15b6142145ad61d28a"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access article titles & url
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["url"] + 2*"\n"
        
body = body.encode("utf-8")
send_email(message=body)