import requests

# print(dir(requests))
text = requests.get("https://www.baidu.com/")

print(text.content)
