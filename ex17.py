import requests
from bs4 import BeautifulSoup

url = "http://www.nytimes.com"
source = requests.get(url)
neat_source_Code = BeautifulSoup(source.text,features="html.parser")

for story_heading in neat_source_Code.find_all(class_="css-6p6lnl"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0])
