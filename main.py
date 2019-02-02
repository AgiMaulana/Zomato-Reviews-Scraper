import scraper
import excel_exporter

urls = [line.rstrip('\n') for line in open('urls.txt')]
review_rates, reviews = [], []
for url in urls:
    # url += '/reviews'
    print('Scrape', url, '....')
    rates, text = scraper.scrap(url)
    review_rates.extend(rates)
    reviews.extend(text)
excel_exporter.export({'rate': review_rates, 'review': reviews})