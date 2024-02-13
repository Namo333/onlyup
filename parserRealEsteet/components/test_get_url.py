from bs4 import BeautifulSoup
import cloudscraper

def getUrl(url, proxy):
    scraper = cloudscraper.create_scraper( 
        interpreter='nodejs', 
        delay=10, 
        browser={ 
            'browser': 'chrome', 
            'platform': 'android', 
            'desktop': False, 
        }, 
    )
    response = scraper.get(url, proxies=proxy)
    print(f"{url} статус: {response.status_code}\n")
    soup = BeautifulSoup(response.text, 'lxml')
    return soup