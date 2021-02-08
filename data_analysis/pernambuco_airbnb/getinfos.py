from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def getConnection(url):
    # WebDriver
    option = Options()
    option.headless = True
    driver = webdriver.Chrome(options=option)

    # Conexão com o site
    driver.get(url)
    driver.implicitly_wait(10)  # in seconds

    # Elementos de classe
    ######################

    elements = driver.find_elements_by_class_name("_8ssblpx")

    return elements


def getData(url, data_list):
    elements = getConnection(url)

    for el in elements:

        get_html = el.get_attribute("innerHTML")
        soup = BeautifulSoup(get_html, "html.parser")

        # COLETAR DADOS DA PÁGINA

        # Tipo de anfitrião
        try:
            superhost = soup.find("div", class_="_ufoy4t").text
        except:
            superhost = "REGULAR"

        #  Localização e tipo de locação
        try:
            room_place = soup.find("div", class_="_b14dlit").text
            place = room_place.split(" em ")[1]
            room = room_place.split(" em ")[0]
        except:
            place = "Not Available"
            room = "Not Available"

        # Título
        try:
            title = soup.find("div", class_="_bzh5lkq").text
        except:
            title = "Not Available"

        # Informações básicas do tipo de locação
        try:
            room_basic = soup.find("div", class_="_kqh46o").text
        except:
            room_basic = "Not Available"

        # Facilidades básicas
        try:
            amenities = soup.findAll("div", class_="_kqh46o")[1].text
        except:
            amenities = "Not Available"

        # Avaliação dos hóspedes
        try:
            rating = soup.find("span", class_="_10fy1f8").text
        except:
            rating = "Not Available"

        # Número de avaliações
        try:
            num_eval = soup.find("span", class_="_a7a5sx").text
        except:
            num_eval = 0

        # Preço (em reais)
        try:
            price = soup.find("span", class_="_olc9rf0").text
        except:
            price = 0

        # URL do imóvel
        try:
            link = soup.select("a")[0]['href']
        except:
            link = "Not Available"

        ## LISTA COM DADOS

        data_list.append([superhost, place, room, title, room_basic,
                          amenities, rating, num_eval, price, link])

    return data_list