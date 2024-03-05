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
    # url = 'https://edition.cnn.com/'
    # # r = requests.get(url)
    # r = session.get(url)
    # html_content = r.text
    # soup = BeautifulSoup(html_content, 'html.parser')

    # ribbon_container_headline = []
    # for i in soup.find_all('div', class_='container__headline container_ribbon__headline'):
    #     if i.get_text().strip() != '':
    #         ribbon_container_headline.append(i.get_text().strip())
    # shuffle(ribbon_container_headline) 


    return render_template('news_index_copy.html')#, headlines=ribbon_container_headline)



if __name__ == '__main__':
    app.run(debug=True)
