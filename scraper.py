import requests
import json

search_keyword = "Pizza"
city = "Madison"
state = "WI"

search_url = "https://www.yelp.com/search/snippet?find_desc=" + search_keyword + "&find_loc=" + city + "%2C+" + state

search_html = requests.get(search_url)

search_results = search_html.text
search_results = json.loads(search_results)
search_results = search_results['searchPageProps']['mainContentComponentsListProps']

for result in search_results:
    if result['searchResultLayoutType'] == "iaResult":
        print("Name: " + result['searchResultBusiness']['name'])
        print("Rating: " + str(result['searchResultBusiness']['rating']))
        print("Review Count: " + str(result['searchResultBusiness']['reviewCount']))
        print("Neighborhoods: " + str(result['searchResultBusiness']['neighborhoods']))
        print("https://www.yelp.com" + result['searchResultBusiness']['businessUrl'])
        print("--------")
        print("")
        