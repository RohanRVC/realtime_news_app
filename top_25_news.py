import requests 
from bs4 import BeautifulSoup
# import pandas as pd  
                   
url = 'https://www.prnewswire.com/news-releases/business-technology-latest-news/business-technology-latest-news-list/'                                          
r = requests.get(url)                                                                          
html_content = r.text                                                                                            
soup = BeautifulSoup(html_content, 'html.parser')                                                                           
                   
                
# To extract the headline, assuming it's within an <h3> tag.              
headline_tags = soup.find_all('h3')                         
          
    
img_tags = soup.find_all('img')      
# Extract the 'src' attribute from each <img> tag       
img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]   
   
# Extract the text from each headline tag.   
headlines = [tag.get_text(strip=True) for tag in headline_tags] 
h=[]
for i in range(len(headlines)):
    h.append(headlines[i]) 
    if i>=24:  
        break 

news_links = soup.find_all('a', class_='newsreleaseconsolidatelink')

# Extract the 'href' attribute from each <a> tag
news_urls = ['https://www.prnewswire.com'+link['href'] for link in news_links if 'href' in link.attrs]

dates = []
titles = []

for item in h:
    # Split the string into two parts at the "ET"
    parts = item.split('ET')
    
    # The first part is the date and time, which we add to the dates list
    date_part = parts[0] if len(parts) > 1 else 'No date found'
    dates.append(date_part.strip())
    
    # The second part, if present, is the headline
    title_part = parts[1] if len(parts) > 1 else 'No title found'
    titles.append(title_part.strip())

# Now we can print or process the separate lists
# print(dates)
# print(titles)
print(img_urls)
# print(news_urls,len(news_urls))
