from flask import render_template,request,redirect,url_for
from app import app
from .request import get_sources,get_articles,search_article

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
    search_article = request.args.get('article_query')
    if search_article:
        return redirect(url_for('search', article_name = search_article))
    else:
        return render_template('articles.html', articles = all_articles, source = source)


@app.route('/search/<article_name>')
def search(article_name):
    """
    Function to display search results
    """
    article_name_list = article_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(article_name_format)
    return render_template('search.html', articles = searched_articles)