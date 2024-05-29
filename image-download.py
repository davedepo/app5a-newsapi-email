# Below code represents steps to download .jpy image from web url

url = "https://www.finextra.com/finextra-images/top_pics/xl/n26-statistics.jpg"

# print(url)
# https://www.finextra.com/finextra-images/top_pics/xl/n26-statistics.jpg

import requests

response = requests.get(url)

print(response)
# returns value in output as - <Response [200]>

# creates binary output value
response.text

with open("image-download-1.jpg", "wb") as file:
	file.write(response.content)
