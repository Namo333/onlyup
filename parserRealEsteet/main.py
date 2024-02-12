import requests

from components.get_url import getUrl
from components.get_item import getItem

url = "https://topaddress.ae/"

proxy = {
   'http': 'http://69.84.182.35:80',
}

def main():
    soup = getUrl(url, proxy)
    nameRealEst = getItem.nameHome(soup)

    for data in nameRealEst:
        print(data)

if __name__ == "__main__":
    main()
    