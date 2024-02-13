class getItem:

    @staticmethod
    def getName(soup):
        homeName = soup.find_all('h3', class_='object-block-title')
        data_list = []
        for h3 in homeName:
            nameLinks = h3.find_all('a')
            for nameAndHref in nameLinks:
                dataName = nameAndHref.text
                data = {'nameEstete': dataName}
                data_list.append(data)
        return data_list
    
    @staticmethod
    def getHref(soup):
        hrefName = soup.find_all('div', class_='object-block-bottom')
        data_list = []
        for href in hrefName:
            hrefLinks = href.find_all('a', class_='object-block-link')
            for nameHref in hrefLinks:
                dataHref = nameHref.get('href')
                href = {'hrefEstete': dataHref}
                data_list.append(href)
        return data_list
    
    @staticmethod
    def getAddres(soup):
        addresName = soup.find_all('div', class_='object-block-location')
        data_list=[]
        for addres in addresName:
            textAddres = addres.find_all('a')
            for addresItem in textAddres:
                addres = {'addresEstete': addresItem.text}
                data_list.append(addres)
        return data_list


    @staticmethod
    def getDeveloper(soup):
        developerName = soup.find_all('div', class_='object-block-developer')
        data_list=[]
        for addres in developerName:
            textAddres = addres.find_all('a')
            for addresItem in textAddres:
                addres = {'developerEstete': addresItem.text}
                data_list.append(addres)
        return data_list

    @staticmethod
    def getRooms(soup):
        roomsName = soup.find_all('div', class_='object-block-container')
        data_list=[]
        for addres in roomsName:
            textAddres = addres.find_all('span', class_='object-block-rooms')
            for addresItem in textAddres:
                addres = {'roomsEstete': addresItem.text}
                data_list.append(addres)
        return data_list

    @staticmethod
    def getSquare(soup):
        squareName = soup.find_all('div', class_='object-block-container')
        data_list=[]
        for addres in squareName:
            textAddres = addres.find_all('span', class_='object-block-square')
            for addresItem in textAddres:
                addres = {'squareEstete': addresItem.text}
                data_list.append(addres)
        return data_list

    @staticmethod
    def getPrice(soup):
        priceName = soup.find_all('div', class_='object-block-price')
        data_list=[]
        for addres in priceName:
            textAddres = addres.find_all('span', class_='price-num')
            for addresItem in textAddres:
                addres = {'priceEstete': f'{addresItem.text}$'}
                data_list.append(addres)
        return data_list

    @staticmethod
    def getImage(soup):
        image_list = []
        blockCont = soup.find_all('div', class_='object-block-holder')
        for aImg in blockCont:
            findImg = aImg.find_all('a', class_='object-block-image')
            for img in findImg:
                imgSrc = img.find_all('img')
                for ansImg in imgSrc:
                    image_url = ansImg.get('src')
                    image_data = {
                        'imageUrlEstete': image_url
                    }
                    image_list.append(image_data)
        return image_list

