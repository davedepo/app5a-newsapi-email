import requests
from send_email import send_email

# to access api_key from newsapi.org
api_key = "fc3a2e50528c42deb19763e8e2cd0113"

topic_key = "+banking", "+technology"
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
# to access articles (check output structure in debugger)
for article in content["articles"][:10]:
	if article["title"] is not None:  # to handle NoneType
		news_content = news_content + (
			f"Date: {article['publishedAt']}" "\n"
			f"Source: {article['source']['name']}" "\n"
			f"Author: {article['author']}" "\n"
			f"Title: {article['title']}" "\n"
			f"Description: {article['description']}" "\n"
			f"Link: {article['url']}\n"
			f"--- end of topic ---" "\n"
			f"\n"
		)

# test iterated output
# print(news_content)

# format email structure
api_source = "https://newsapi.org"
subject_line = (f"🌞 Good Morning! Your Daily News Brief: Banking and "
                f"Technology Updates 📰 (in dev stage)")
news_content = f"""\
Subject: {subject_line}

List of 10 news articles from {api_source} are below:

{news_content}
"""
# test email output
print(news_content)

# .encode is required to call send_email() else disable line to run print()
news_content = news_content.encode("utf-8")

# send email
send_email(message=news_content)
