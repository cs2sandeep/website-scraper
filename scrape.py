import requests
from bs4 import BeautifulSoup

print('a')
response = requests.get("https://news.ycombinator.com")
print('b')
soup = BeautifulSoup(response.text, 'html.parser')

site_links = soup.select('.titleline > a')
site_votes = soup.select('.score')

def create_custom_hn(links, votes):
    hn = []
    for index, element in enumerate(links):
        title = element.getText()
        link = element.get('href', None)

        points = int(site_votes[index].getText().removesuffix(' points'))

        hn.append({'title': title, 'link': link, 'points': points})
    return hn

print(create_custom_hn(site_links, site_votes))
print(len(create_custom_hn(site_links, site_votes)))