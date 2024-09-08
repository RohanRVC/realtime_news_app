import requests
from bs4 import BeautifulSoup
# import pandas as pd
   
url = 'https://techcrunch.com/'  
r = requests.get(url)    
html_content = r.text     
soup = BeautifulSoup(html_content, 'html.parser')  
# print(soup)  
# container__headline-text       
 
li=[]    
main_text='' 
img=[] 
for i in soup.find_all('a', class_="post-block__title__link"): 
    # print(i.get_text())    
    main_text+=i.get_text()
    break   
img_tag = soup.find('img')
img_link = img_tag['src'] if img_tag else 'No image found'
a_tag = soup.find('a', class_='post-block__title__link')
# If there's no class to search by, just find any <a> tag within the <figure>
if not a_tag:
    figure = soup.find('figure', class_='post-block_media')
    if figure:
        a_tag = figure.find('a')

# Extract the 'href' attribute
if a_tag and 'href' in a_tag.attrs:
    hyperlink = a_tag['href']
else:
    hyperlink = 'No hyperlink found'


time_element = soup.find('span', class_='article__byline__meta__slash')
# datetime_attribute = time_element['datetime'] if time_element else 'No datetime found'
# date_text = time_element.text if time_element else 'No date text found'
# print("Datetime attribute:", datetime_attribute)
# print("Date text:", date_text)
print(time_element)
