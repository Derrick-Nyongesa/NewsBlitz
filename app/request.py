from app import app
import urllib.request,json
from .models import sources

Sources = sources.Sources

api_key = app.config['NEWS_API_KEY']

base_url = app.config['NEWS_API_BASE_URL']

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
