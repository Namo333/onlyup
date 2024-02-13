import requests
import json

from components.get_url import getUrl
from components.get_item import getItem

url = "https://topaddress.ae/dubai-apartments-for-sale/"

proxy = {
   'http': 'http://69.84.182.35:80',
}

def main():
    soup = getUrl(url, proxy)
    nameRealEst = getItem.getName(soup)
    addresRealEst = getItem.getAddres(soup)
    developerRealEst = getItem.getDeveloper(soup)
    roomsRealEst = getItem.getRooms(soup)
    squareRealEst = getItem.getSquare(soup)
    priceRealEst = getItem.getPrice(soup)
    imageRealEst = getItem.getImage(soup)

    data_list = []
    for idx, data in enumerate(nameRealEst, start=1):
        data_dict = {
            "id": idx,
            "nameEstete": data['nameEstete'],
            "addresEstete": addresRealEst[idx - 1]['addresEstete'] if addresRealEst and idx <= len(addresRealEst) else None,
            "developerEstete": developerRealEst[idx - 1]['developerEstete'] if developerRealEst and idx <= len(developerRealEst) else None,
            "roomsEstete": roomsRealEst[idx - 1]['roomsEstete'] if roomsRealEst and idx <= len(roomsRealEst) else None,
            "squareEstete": squareRealEst[idx - 1]['squareEstete'] if squareRealEst and idx <= len(squareRealEst) else None,
            "priceEstete": priceRealEst[idx - 1]['priceEstete'] if priceRealEst and idx <= len(priceRealEst) else None,
            "imageUrlEstete": imageRealEst[idx - 1]['imageUrlEstete'] if imageRealEst and idx <= len(imageRealEst) else None
        }
        data_list.append(data_dict)

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data_list, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()