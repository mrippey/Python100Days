from flask import Flask, render_template
from flask_table import Table, Col 
from bs4 import BeautifulSoup 
import requests 


site = "https://www.wired.com"


app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    errors = []
    title = []
    author = []
    try:
        response = requests.get(site)
        response.raise_for_status()
    except ConnectionError as e:
        errors.append(e)
        return render_template('index.html', errors)

    if response:
        soup = BeautifulSoup(response.text, 'html.parser')
        art_byline = soup.find_all(class_='post-listing-list-item__description')[:7]

        for items in art_byline:
            titles = items.h5.getText()
            authors = items.find('span', class_='byline-component__content').text

            title.append(titles)
            author.append(authors)
            
                        

    return render_template('index.html', errors = errors, var1=title, var2=author)

if __name__ == "__main__":
    app.run(debug=True)
