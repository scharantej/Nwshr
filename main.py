
# main.py

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/news')
def news():
    api_key = 'YOUR_API_KEY'
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(api_key)
    response = requests.get(url)
    articles = response.json()['articles']
    return render_template('index.html', articles=articles)

@app.route('/article/<id>')
def article(id):
    api_key = 'YOUR_API_KEY'
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(api_key)
    response = requests.get(url)
    articles = response.json()['articles']
    article = [a for a in articles if a['id'] == id][0]
    return render_template('article.html', article=article)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
