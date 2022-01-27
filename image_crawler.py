from urllib import request
import requests as re
from bs4 import BeautifulSoup as bs
import os

url = input('주소 입력 :')
# 예시 url = "https://ohou.se/productions/628174/selling"

res = re.get(url = url)
soup = bs(res.content, 'html.parser')
# 사진을 보관할 directory 만들기
name = soup.find(class_="production-selling-header__title__brand").text
name = str(name).strip()
current_path = os.getcwd()
try: 
    if not os.path.exists(current_path + "/" + name): 
        os.mkdir(current_path + "/" + name)
except OSError: 
    print("Error: Cannot create the directory {}".format(current_path + "/" + name))
new_path = current_path + "/" + name + "/"
# 이미지 크롤링
img = soup.find_all(class_='image')
n = 1
for i in img:
    with re.get(i['src'].split('?')[0]) as u:
        with open(new_path + str(n) + '.jpg', 'wb') as file:
            file.write(u.content)
    n += 1
print("완료되었습니다.")