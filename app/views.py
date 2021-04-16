from flask import render_template
from app import app
from .request import get_sources

@app.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    general_news = get_sources('general')
    business_news = get_sources('business')
    sports_news = get_sources('sports')
    title = 'Home - Welcome to the NewsBlitz'
    return render_template('index.html', title = title, general = general_news)