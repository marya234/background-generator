import requests
from bs4 import BeautifulSoup

print('heello')
# URL = 'https://news.ycombinator.com/'
# for page in range(2,3):
#     res = requests.get(URL + '/' + 'newws?p=' + str(page))
#     soup = BeautifulSoup(res.text, 'html.parser')
#     links = soup.select('.titlelink')
#     subtext = soup.select('.subtext')
#
#     def sort_stories_by_votes(hnlist):
#         return sorted(hnlist, key=lambda  k:k['votes'], reverse=True)
#
#     def create_custom_hn(links,subtext):
#         hn = []
#         for idx, item in enumerate(links):
#             title = item.getText()
#             href = item.get('href', None)
#             vote = subtext[idx].select('.score')
#             if len(vote):
#                 points = int(vote[0].getText().replace(' points', ''))
#                 if points > 99:
#                     hn.append({'title': title, 'link': href, 'votes': points})
#         return sort_stories_by_votes(hn)
#
#     print(create_custom_hn(links,subtext))