import requests
import re
from bs4 import BeautifulSoup
import json

User_Agent_head = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
english_result = []

# WORLD HISTORY ENCYCLOPEDIA에서 ukraine를 검색한 결과를 크롤링하였습니다.

def createJs(title, result): # json 파일로 변경
  with open('{}.json'.format(title), 'w', encoding = "UTF-8-sig") as f_write:
    json.dump(result, f_write, ensure_ascii = False, indent = 4)

  data = ""
  with open('{}.json'.format(title), "r", encoding = "UTF-8-sig") as f:
    line = f.readline()
    while line:
      data += line
      line = f.readline()

class Req:
    def __init__(self, contents):
        self.url = contents.get("urls")
        
    def send_message(self):
        print(self.url)
        return 0
        


def google_params():
    keys = ('urls', 'keyword', 'language')
    values = (
        'https://www.google.com/search?q={}&hl=ko&tbm=nws&ei=4eMlYunIJNyUr7wPnrm0oAo&start={}&sa=N&ved=2ahUKEwipvcTD6rP2AhVcyosBHZ4cDaQ4KBDy0wN6BAgBED8&biw=1920&bih=937&dpr=1'
        , 'ukraine negotiation'
        , 'ko'
    )
    return dict(zip(keys, values))

if __name__ == "__main__": 
    google_search = Req(google_params())
    google_search.send_message()
    
    
    
