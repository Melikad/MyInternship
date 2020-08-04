from Melika.Lyrics.main.src.core.crawler.fetcher.genius_fetcher import GeniusFetcher

token = 'PkpPAi-QNRocHlidtc3tCwU4jY1BA7IIJZwHzBjsfJCgvbq1BiyXMhFL-xm8ftRX'


fetcher = GeniusFetcher(10, 10, 10, token)
response = fetcher.fetch_artist_songs('1177')

with open('D:/Desktop/output.txt', 'w', encoding='utf8') as file:
    file.write(response.text)

