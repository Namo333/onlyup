class getItem:
    @staticmethod
    def nameHome(soup):
        homeNameAddres = soup.find_all('h3', class_='object-block-title')
        data_list = []
        for h3 in homeNameAddres:
            nameLinks = h3.find_all('a')
            for nameAndHref in nameLinks:
                dataName = nameAndHref.text
                dataHref = nameAndHref.get('href')
                data = f"{dataHref} - {dataName}"
                data_list.append(data)
        return data_list