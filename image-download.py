# Below code represents steps to download .jpy image from web url

url = "https://www.finextra.com/finextra-images/top_pics/xl/n26-statistics.jpg"

# print(url)
# https://www.finextra.com/finextra-images/top_pics/xl/n26-statistics.jpg


# import requests module
import requests

# get binary data from url
response = requests.get(url)

# print response output i.e. of binary data
print(response)  # output - <Response [200]>

# creates binary output value
response.text

# download image in project dir
with open("image-download-1.jpg", "wb") as file:
	file.write(response.content)
