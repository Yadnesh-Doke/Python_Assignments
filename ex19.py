import requests
from bs4 import BeautifulSoup

base_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
source = requests.get(base_url)
neat_source_Code = BeautifulSoup(source.text,features="html.parser")

all_p = neat_source_Code.select("p")

for elem in all_p[7:]:
    # print("inside for loop")
    print(elem.text)
