import scraper

urls = [
    'https://www.zomato.com/id/bandung/ayam-geprek-bebas-dago/reviews',
    'https://www.zomato.com/id/bandung/kandang-ayam-pasirkaliki/reviews'
    'https://www.zomato.com/id/bandung/bellamie-boulangerie-riau/reviews'
    'https://www.zomato.com/id/bandung/monsoon-sukajadi/reviews'
]

[scraper.scrap(url) for url in urls]