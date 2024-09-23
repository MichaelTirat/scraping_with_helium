from bs4 import BeautifulSoup
import re
import numpy as np

def scrap_price(element):
    soup = BeautifulSoup(element.web_element.get_attribute('innerHTML'), 'html.parser')
    row = soup.find('span', class_='a-size-base a-color-price')
    try :
        if row:
            return float(row.text[:-2].replace(',', '.'))
        else:
            return np.nan
    except:
        return np.nan


def scrap_votes(element):
    soup = BeautifulSoup(element.web_element.get_attribute('innerHTML'), 'html.parser')
    html_vote = soup.find('i', class_='a-icon')
    if html_vote:
        try:
            valid_vote = float(re.sub(r'\s+', '', html_vote.text.split(' ')[0].replace(',', '.')))
            return valid_vote
        except ValueError :
            return 0
    else :
        return 0


def scrap_nb_votes(element):
    soup = BeautifulSoup(element.web_element.get_attribute('innerHTML'), 'html.parser')
    search_nb_votes = soup.find('span', class_='a-size-small')

    if search_nb_votes:
        try:
            # Nettoyage du texte et conversion en entier
            numeric_value = int(re.sub(r'\s+', '', search_nb_votes.text))
            return numeric_value
        except ValueError:
            # En cas de problème de conversion
            return 0
    else:
        # Si aucun élément 'span' avec la classe spécifiée n'est trouvé
        return 0

