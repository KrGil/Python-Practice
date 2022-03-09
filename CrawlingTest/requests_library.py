import requests

# response = requests.get("https://www.naver.com")
response = requests.get("https://www.law.go.kr/법령/민법")
html = response.text
print(html)