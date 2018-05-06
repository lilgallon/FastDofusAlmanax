from bs4 import BeautifulSoup
import datetime
from time import strptime
from lxml import html
import requests


def main():

    print(">> FAST DOFUS ALMANAX v0.1 -- N3RO <<")
    url = "http://www.krosmoz.com/fr/almanax/"
    
    session = requests.session()
    results = connect(url, session)

    if results is None:
        return

    soup = BeautifulSoup(results[1].content, "html.parser")

    main_container = (soup.find_all("div", id="achievement_dofus")[0]
                          .find("div", class_="mid")
                          .find("div", class_="more"))

    bonus = main_container.text.replace("\n", "").replace("\t", " ").split('Quête')[0]
    almanax = main_container.find('p', class_="fleft").text.replace("\n", " ").replace("\t", "")

    print("BONUS >> " + bonus)
    print("OFFRANDE >> " + almanax)
    input('Press ENTER to exit')


def connect(url, session):

    print("Connection à " + url + " ...")

    result = session.get(
        url,
        headers=dict(referer=url))

    if result.ok:
        print('Connection réussie')
        return [session, result]
    else:
        print('Connection échouée')
        return None

if __name__ == '__main__':
    main()