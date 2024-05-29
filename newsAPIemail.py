import requests
from send_email import send_email

# to access api_key from newsapi.org
api_key = "fc3a2e50528c42deb19763e8e2cd0113"

# to access endpoint url for Tesla news (from newsapi.org)
# update from=date before run
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-04-29&sortBy=publishedAt&" \
      "apiKey=fc3a2e50528c42deb19763e8e2cd0113"

# make request to endpoint url
request = requests.get(url)

# to get output as dict replace .text to .json()
content = request.json()
print(content)

news_content = ""
# to access article - titles & description (check output structure in debugger)
for article in content["articles"]:
	# if article["title"] is not None: -- to handle NoneType
	news_content = news_content + (f"News source: {article['source']}" "\n"
	                               f"Title: {article['title']}" "\n"
	                               f"Description: {article['description']}" "\n"
	                               f"\n"
	                               f"--- end of article ---" "\n")

api_source = "https://newsapi.org"
news_topic = "Tesla"
news_content = f"""\
Subject: News Email Digest (in dev stage) - {news_topic}

From: api source - {api_source}

{news_content}
"""

news_content = news_content.encode("utf-8")
send_email(message=news_content)
