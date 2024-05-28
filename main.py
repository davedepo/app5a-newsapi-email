import requests
from send_email import send_email


# to access api_key from newsapi.org
api_key = "fc3a2e50528c42deb19763e8e2cd0113"

# to access endpoint url for Tesla news (from newsapi.org)
url = "https://newsapi.org/v2/everything?q=tesla&" \
	  "from=2024-04-28&sortBy=publishedAt&" \
	  "apiKey=fc3a2e50528c42deb19763e8e2cd0113"

# make request to endpoint url
request = requests.get(url)

# to get output as dict replace .text to .json()
content = request.json()
print(content)


body = ""
# to access article - titles & description (check output structure in debugger)
for article in content["articles"]:
	if article["title"] is not None:
		body = f"{body}\nTitle: {article["title"]}\n"\
			   f"Description: {article["description"]}\n\n"

body = body.encode("utf-8")
send_email(message=body)
