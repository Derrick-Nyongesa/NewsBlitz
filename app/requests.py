import urllib.request,json
from .models import Sources, Articles


api_key = None

base_url = None

articles_base_url = None

search_url = None

def configure_request(app):
    global api_key, base_url, articles_base_url, search_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_base_url = app.config['ARTICLES_API_BASE_URL']
    search_url = app.config['SEARCH_API_BASE_URL']

def get_sources(category):
    """
    function that gets response from the api call
    """    
    sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(sources_url) as url:
        sources_data = url.read()
        sources_response = json.loads(sources_data)

        sources_results = None

        if sources_response['sources']:
            sources_results_list = sources_response['sources']
            sources_results = process_results(sources_results_list)
    return sources_results

def process_results(sources_list):
    """
    Function  that processes the movie result and transform them to a list of Objects
    """
    sources_results = []

    for one_source in sources_list:
        id = one_source.get("id")
        name = one_source.get("name")
        description = one_source.get("description")
        url = one_source.get("url")
        category = one_source.get("category")
        language = one_source.get("language")
        country = one_source.get("country")
        
        source_object = Sources(id,name,description,url,category,country)
        sources_results.append(source_object)
    
    return sources_results


def get_articles(source):
    """
    Function that gets the json response to our url request
    """
    articles_url = articles_base_url.format(source, api_key)

    with urllib.request.urlopen(articles_url) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data)

        articles_results = None

        if articles_response['articles']:
            articles_list = articles_response['articles']
            articles_results = process_articles(articles_list)
    return articles_results

def process_articles(article_list):
    articles_results = []
    for article_item in article_list:
        source = article_item.get("source")
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        
        article_object = Articles(source,author,title,description,url,urlToImage,publishedAt)
        articles_results.append(article_object)
    return articles_results



def search_article(article_name):
    search_article_url = search_url.format(article_name,api_key)

    with urllib.request.urlopen(search_article_url) as url:
        search_data = url.read()
        search_response = json.loads(search_data)

        search_results = None

        if search_response['articles']:
            search_list = search_response['articles']
            search_results = process_articles(search_list)
    return search_results 
