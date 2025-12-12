# REST API (Representational State Transfer API) to styl architektoniczny
# dla budowania usług internetowych, który używa standardowych
# żądań HTTP do komunikacji między systemami, traktując dane jako zasoby,
# którymi można zarządzać za pomocą metod takich jak GET, POST, PUT i DELETE,
# typowo wymieniając dane w formacie JSON.
import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)
print(response)  # <Response [200]>
# 200 ok
# 3xx - warningi, przekierowania
# 4xx - 404 - brak zasobu, 400 Bad Requests - błąd w parametrach
# 5xx błedy serwera 500 Internal Server Error

print(response.text)
data = response.json()
print(data)
print(type(data))
print(data['value'])
# Chuck Norris can blow bubbles with beef jerky.

for key in data:
    print(key)
# categories
# created_at
# icon_url
# id
# updated_at
# url
# value

response_img = requests.get(data['icon_url'])
with open("icon.png", "wb") as f:
    f.write(response_img.content)