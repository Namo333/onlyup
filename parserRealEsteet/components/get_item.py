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
    def getAddres(soup):
        pass

    @staticmethod
    def getDeveloper(soup):
        pass

    @staticmethod
    def getRooms(soup):
        pass

    @staticmethod
    def getSquare(soup):
        pass

    @staticmethod
    def getPrice(soup):
        pass

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

