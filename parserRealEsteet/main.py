from bs4 import BeautifulSoup
import cloudscraper
import requests

url = "https://topaddress.ae/"

proxy = {
   'http': 'http://69.84.182.35:80',
}

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
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def findH1(soup):
    h3_elements = soup.find_all('h3', class_='object-block-title')
    for h3 in h3_elements:
        a_tag = h3.find('a')
        if a_tag:
            print(a_tag.text)

def main():
    soup = getUrl(url, proxy)
    findH1(soup) 

if __name__ == "__main__":
    main()
    