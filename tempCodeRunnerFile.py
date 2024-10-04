# import json

# import requests as rq
# API_KEY = "61f0041981ac4b8eb0e45938240308"
# data = rq.get(f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q=toshkent")
# data = data.text
# data = json.loads(data)

# print(data['current']['temp_c'])

from pytubefix import YouTube

# YouTube video URL
url = "https://youtu.be/d_S6HyolN_w?si=YtmFdOzpqumLssG0"

# Video obyekti yarating
yt = YouTube(url)

# Video haqida ma'lumot chop etish
print(f"Title: {yt.title}")
print(f"Views: {yt.views}")
print(f"Length: {yt.length} seconds")

# Yuklab olish
video = yt.streams.get_highest_resolution()
video.download()

print("Video muvaffaqiyatli yuklandi!")
