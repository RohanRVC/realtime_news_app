import requests
from bs4 import BeautifulSoup   
   
url = 'https://www.prnewswire.com/news-releases/flash-news-okx-ventures-announces-series-a-investment-in-taiko-a-decentralized-ethereum-equivalent-zk-rollup-302076975.html'
url='https://www.prnewswire.com/news-releases/southwest-orthopaedic-specialists-pllc-notifies-of-integris-health-data-security-incident-302077690.html' 
r = requests.get(url)
html_content = r.text 
soup = BeautifulSoup(html_content, 'html.parser')  
# print(soup) 
# container__headline-text
title_element = soup.find('div', class_="col-sm-8 col-vcenter col-xs-12") 
     
    # Extract the text from the title element 
title_text = title_element.get_text(strip=True) if title_element else 'Title not found'
    
    # Print the title text 
# print(title_text) 

# Extract the URL from the 'src' attribute of the <img> tag
img_tags = soup.find_all('img')
# Extract the 'src' attribute from each <img> tag
img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]
# print(img_urls) 
new_link=[]
for i in img_urls:
    if i.startswith('htt') and i.endswith('nail'):
        new_link.append(i)

text=''
for  i in soup.find_all('div',class_='col-lg-10 col-lg-offset-1'): 
        
        text+=i.get_text()
        if "SOURCE"  in i.get_text():
             break


