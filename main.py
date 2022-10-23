from flask import (
    Flask, 
    render_template, 
    request,
    )
import requests
from bs4 import BeautifulSoup
from address import address

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html', address=address)

@app.route('/search', methods=['POST'])
def search():
    url = request.form.get('url')
    if url == None:
        url = 'https://mystat.itstep.org/ru/main/dashboard/page/index'
    response = requests.get(url)
    s = BeautifulSoup(response.text, "html")
    address.append(s.find_all('html'))
    return render_template('search.html')

if __name__ == "__main__":
    app.run(debug=True, port=1234)