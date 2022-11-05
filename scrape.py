import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com")
soup = BeautifulSoup(response.text, 'html.parser')

site_links = soup.select('.titleline > a')
site_votes = soup.select('.score')

def create_custom_hn(links, votes):
    hn = []
    for index, element in enumerate(links):
        title = element.getText()
        link = element.get('href', None)

        points = int(votes[index].getText().removesuffix(' points'))

        hn.append({'title': title, 'link': link, 'points': points})
    return hn


def more_than_100(posts):
    pop_posts = []
    generator1 = filter(lambda post: post['points'] > 100, posts)
    for item in generator1:
        pop_posts.append(item)
    return pop_posts

all_posts = create_custom_hn(site_links, site_votes)
print(more_than_100(all_posts))