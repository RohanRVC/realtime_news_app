from flask import Flask, render_template,request,abort
import requests
from bs4 import BeautifulSoup
from random import shuffle

app = Flask(__name__)


# Create a session object
session = requests.Session()
# Set 'keep_alive' to False
session.keep_alive = False

@app.route('/')
def home():
    url = 'https://edition.cnn.com/'
    # r = requests.get(url)
    r = session.get(url)
    html_content = r.text
    soup = BeautifulSoup(html_content, 'html.parser')

    ribbon_container_headline = []
    for i in soup.find_all('div', class_='container__headline container_ribbon__headline'):
        if i.get_text().strip() != '':
            ribbon_container_headline.append(i.get_text().strip())
    shuffle(ribbon_container_headline) 

    url = 'https://techcrunch.com/'
    r = requests.get(url)
    html_content = r.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # Initialize variables to store the title and image
    main_text = ''
    img_link = ''
    hyperlink = ''

    # Find the main text and image
    main_text_tag = soup.find('a', class_="post-block__title__link")
    if main_text_tag:
        main_text = main_text_tag.get_text(strip=True)

    img_tag = soup.find('img')
    if img_tag and 'src' in img_tag.attrs:
        img_link = img_tag['src']

    a_tag = soup.find('a', class_='post-block__title__link')
    if a_tag and 'href' in a_tag.attrs:
        hyperlink = a_tag['href']
    


    url3 = 'https://www.prnewswire.com/news-releases/business-technology-latest-news/business-technology-latest-news-list/?page=1&pagesize=100'
    r3 = requests.get(url3)
    html_content3 = r3.text
    soup3 = BeautifulSoup(html_content3, 'html.parser')


    # To extract the headline, assuming it's within an <h3> tag.
    headline_tags = soup3.find_all('h3')


    # # img_tags = soup.find_all('img')
    # # # Extract the 'src' attribute from each <img> tag
    # # img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]

    # Extract the text from each headline tag.
    headlines = [tag.get_text(strip=True) for tag in headline_tags]
    h=[]
    for i in range(len(headlines)):
        h.append(headlines[i])
        if i>=99:
            break

    news_links = soup3.find_all('a', class_='newsreleaseconsolidatelink')

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

    news_items = zip(dates, titles, news_urls)

    return render_template('news_index.html', main_text=main_text, img_link=img_link, hyperlink=hyperlink, headlines=ribbon_container_headline,news_items=news_items)


@app.route('/dynamic_article1')
def dynamic_article1():
    # Get the article URL from the query parameter
    article_url = request.args.get('url')
    
    # Validate the URL before making a request to it, for security reasons
    if not is_valid_url(article_url):  # You should implement the is_valid_url function
        abort(400)  # Bad request
    
    try:
        # Fetch the article content
        # response = requests.get(article_url)
        response = requests.get(article_url)

        soup = BeautifulSoup(response.content, 'html.parser')

        # Scrape the title
        title_text = soup.find('h1',class_="article__title")
       
        
        img_tag=soup.find('img')#,class_='article__featured-image article__featured-image--block')
        img_urls= img_tag['src'] if img_tag else 'No image found'

        content_tag=soup.find_all('p')
        content_text=''
        for i in content_tag:
            content_text+=i.get_text()

        title=title_text.get_text()

        # Pass scraped data to the template
        return render_template('dynamic_article1.html', title=title, images=img_urls, content=content_text)
    except Exception as e:
        # Log the error e
        abort(500)  # Internal server error



@app.route('/dynamic_article')
def dynamic_article():
    # Get the article URL from the query parameter
    article_url = request.args.get('url')
    
    # Validate the URL before making a request to it, for security reasons
    if not is_valid_url(article_url):  # You should implement the is_valid_url function
        abort(400)  # Bad request
    
    try:
        # Fetch the article content
        # response = requests.get(article_url)
        response = requests.get(article_url)

        soup = BeautifulSoup(response.content, 'html.parser')

        # Scrape the title
        title_element = soup.find('div', class_="col-sm-8 col-vcenter col-xs-12")
        title_text = title_element.get_text(strip=True) if title_element else 'Title not found'

        # Scrape all images
        img_tags = soup.find_all('img')
        img_urls = [img['src'] for img in img_tags if 'src' in img.attrs and img['src'].startswith('http') and 'thumbnail' in img['src']]

        # Scrape the content until "SOURCE" text
        content_element = soup.find('div', class_='col-lg-10 col-lg-offset-1')
        content_text = ''
        for element in content_element.find_all('p', recursive=False):  # Assuming content paragraphs are direct children
            if "SOURCE" in element.get_text():
                break
            content_text += element.get_text()

        # Pass scraped data to the template
        return render_template('dynamic_article.html', title=title_text, images=img_urls, content=content_text)

    except Exception as e:
        # Log the error e
        abort(500)  # Internal server error

# Implement a function to validate the URL
def is_valid_url(url):
    # Simple HTTP/HTTPS check. For production use, this should be more robust.
    return url.startswith('http://') or url.startswith('https://')



if __name__ == '__main__':
    app.run(debug=True)
