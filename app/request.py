from app import app
import urllib.request,json
from .models import sources

Sources = sources.Sources

api_key = app.config['NEWS_API_KEY']

base_url = app.config['NEWS_API_BASE_URL']

def get_sources(category):
    """
    Function that gets response from the api call
    """
    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['results']:
            sources_results_list = get_sources_response['results']
            sources_results = process_results(sources_results_list)


    return sources_results


def process_results(sources_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects
    '''
    sources_results = []
    for news_item in sources_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        country = news_item.get('country')

        source_object = Sources(id,name,description,url,category,country)
        sources_results.append(source_object)

    return movie_results