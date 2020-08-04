import requests
import json
from bs4 import BeautifulSoup
import re

"""
session = requests.Session()
session.headers.update({'authorization': 'Bearer ' + 'uZRt2lRoFq5wCE2_WG6oWCdyqlMABdAW3zRBMKiB1sMxVbKhCbqy-vzFdDJbE1SD'})
# response = session.get('https://api.genius.com/search', params={'q':'Queens'})
response = session.get('https://api.genius.com/songs/2270213')


print(response.text)
with open('song.json', 'w', encoding='utf8') as file:
    file.write(response.text)
"""

lyrics = requests.get('https://genius.com/Billie-eilish-my-future-lyrics').text

soup = BeautifulSoup(lyrics, 'html.parser')
content = soup.find('html').find('head').find_all('meta')[25].get('content')
lyrics = json.loads(content)['lyrics_data']['body']['html']


def clean_lyrics(lyrics: str) -> lyrics:
    lyrics = re.sub(r'<(\"[^\"]*\"|\'[^\']*\'|[^\'\">])*>', '', lyrics)
    lyrics = re.sub(r'\[.+?\]', '', lyrics)
    lyrics = re.sub(r'\(.+?\)', '', lyrics)
    lyrics = re.sub(r'[\'\"?.!:,]', '', lyrics)
    return lyrics.strip()


# print(lyrics)
# with open('data.json', 'w+', encoding='utf8') as file:
#     file.write(content)

with open('lyrics.txt', 'w+', encoding='utf8') as file:
    file.write(clean_lyrics(lyrics))
