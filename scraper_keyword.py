import requests
from bs4 import BeautifulSoup
import pandas as pd   

url = 'https://edition.cnn.com/'
r = requests.get(url)   
html_content = r.text   
soup = BeautifulSoup(html_content, 'html.parser') 
# print(soup) 
# container__headline-text
 
ribbon_container_headline=[]
  
for i in soup.find_all('div', class_='container__headline container_ribbon__headline'):  
    # print(i.get_text())
    if i!='\n':
        ribbon_container_headline.append(i.get_text())
 
ribbon_container_headline = [item.strip() for item in ribbon_container_headline]

print(ribbon_container_headline)
 
