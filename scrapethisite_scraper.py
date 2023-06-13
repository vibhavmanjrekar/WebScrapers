import urllib.request
from bs4 import BeautifulSoup as soup

url = 'https://www.scrapethissite.com/pages/simple/'

req = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

url_client = urllib.request.urlopen(req)
page_html = url_client.read()
url_client.close()
page_soup = soup(page_html, 'html.parser')
countries = page_soup.findAll('div', {"class": "row"})

for country in countries:
    country_html = country.findAll("h3", {"class": "country-name"})
    country_info_html = country.findAll("div", {"class": "country-info"})
    for field in range(len(country_html)):
        country_name = country_html[field].text.strip()
        country_info = country_info_html[field].text.strip()
        print(country_name)
        print(country_info)
        print()

