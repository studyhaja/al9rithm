import requests
url = "https://i.pinimg.com/474x/4e/b4/0e/4eb40ee3b3c281ab9d9e05385cf9de3f.jpg"
result = requests.get(url)

with open("new_photo.jpg", "wb") as f:
    f.write(result.content)
    f.close()