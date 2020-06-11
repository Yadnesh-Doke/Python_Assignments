import requests
from bs4 import BeautifulSoup

url = "http://www.nytimes.com"
r = requests.get(url)
soup = BeautifulSoup(r.text,features="html.parser")

for story_heading in soup.find_all(class_="css-6p6lnl"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0])
