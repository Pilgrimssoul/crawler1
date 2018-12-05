import requests, re
from bs4 import BeautifulSoup

date = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}
response = requests.get("https://www.sohu.com/a/76928120_406463", headers=date)
if response.status_code == 200:
    html = response.content.decode('utf-8')
    # print(html)
    soup = BeautifulSoup(html, "lxml")

print(soup.find('head'))
