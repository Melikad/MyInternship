from Melika.Lyrics.main.src.core.crawler.fetcher.genius_fetcher import GeniusFetcher

token = 'PkpPAi-QNRocHlidtc3tCwU4jY1BA7IIJZwHzBjsfJCgvbq1BiyXMhFL-xm8ftRX'


fetcher = GeniusFetcher(10, 10, 10, token)
response = fetcher.fetch_search_results('billie eilish')

with open('output.json', 'w', encoding='utf8') as file:
    file.write(response.text)

