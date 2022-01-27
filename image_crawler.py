from urllib import request
import requests as re
from bs4 import BeautifulSoup as bs
import os

# path =r'C:\Users\JUNYUB\Desktop\Start Up\ohouse_image_crawler\img'
# os.mkdir(path)

# url = input('주소 입력 :')
url = "https://ohou.se/productions/309019/selling"

res = re.get(url = url)
soup = bs(res.content, 'html.parser')
img = soup.find_all(class_='image')
n = 1
for i in img:
    with re.get(i['src'].split('?')[0]) as u:
        with open('C:/Users/JUNYUB/Desktop/Start Up/ohouse_image_crawler/img/' + str(n) + '.jpg', 'wb') as file:
            file.write(u.content)
    n += 1
