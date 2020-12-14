import json
from bs4 import BeautifulSoup
import requests

url = "http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/"
web = requests.get(url)
Out = BeautifulSoup(web.content, 'html.parser')


# ULTRAMAN
index = []
name_ultra = []
ultraman = {}
for i in Out.find_all('p' and 'strong'):
    text = i.text
    if text[:2].isdigit():
        ultra_index = text[:2]
        ultra_name = text[3:]
        temp_dict = {ultra_index: ultra_name}
        ultraman.update(temp_dict)
    elif "Ultra Monster" in text:
        break
    else:
        continue

# ULTRAMONSTER
index = []
name_ultra = []
ultramonster = {}
for i in Out.find_all('p' and 'strong'):
    text = i.text
    if text[:2].isdigit():
        ultra_index = text[:2]
        ultra_name = text[3:]
        temp_dict = {ultra_index: ultra_name}
        ultramonster.update(temp_dict)
    else:
        continue

ultraman = [{"Ultraman": ultraman, "Monster": ultramonster}]

# export to json
with open("20201214_stats_python_web_scraping_ultraman.json", "w") as file:
    json.dump(ultraman, file)

print('file json created')
