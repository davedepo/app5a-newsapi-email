import requests
from send_email import send_email

# to access api_key from newsapi.org
api_key = "fc3a2e50528c42deb19763e8e2cd0113"


topic_key = "tesla"
# to access endpoint url for Tesla news (from newsapi.org)
# if required add from=date before run: "from=2024-04-29&" \
url = "https://newsapi.org/v2/everything?" \
      f"q={topic_key}&" \
	  "sortBy=publishedAt&" \
      "apiKey=fc3a2e50528c42deb19763e8e2cd0113&" \
	  "language=en"

# make request to endpoint url
request = requests.get(url)

# to get output as dict replace .text to .json()
content = request.json()
print(content)

news_content = ""
# to access article - titles & description (check output structure in debugger)
for article in content["articles"][:20]:
	# if article["title"] is not None: -- to handle NoneType
	news_content = news_content + (f"Source: {article['source']['name']}" "\n"
	                               f"Title: {article['title']}" "\n"
	                               f"Description: {article['description']}" "\n"
	                               f"Link: {article['url']}\n"
	                               f"\n"
	                               f"--- end of topic ---" "\n")

api_source = "https://newsapi.org"
news_topic = "Tesla"
news_content = f"""\
Subject: Today's News (in dev stage) - {news_topic}

From: api source - {api_source}

{news_content}
"""

# .encode is required to call send_email() else disable line to run print()
news_content = news_content.encode("utf-8")
send_email(message=news_content)
