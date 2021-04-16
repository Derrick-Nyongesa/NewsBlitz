from flask import render_template
from app import app
from .request import get_sources,get_articles

@app.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    general_news = get_sources('general')
    business_news = get_sources("business")
    entertainment_news = get_sources("entertainment")
    sports_news = get_sources("sports")
    title = 'Home - Welcome to NewsBlitz'
    return render_template('index.html',title=title,general=general_news,business=business_news,entertainment=entertainment_news,sports=sports_news )


@app.route('/articles/<id>')
def article(id):
    """
    View page thar returns news articles from a source
    """
    all_articles = get_articles(id)
    print(all_articles)
    source = id
    return render_template('articles.html', articles = all_articles, source = source)