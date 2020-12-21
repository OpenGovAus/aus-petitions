import json
from requests import get
from bs4 import BeautifulSoup

CURRENT_PETITIONS = 'https://parliament.nt.gov.au/business/petitions-and-responses'

def all_petitions():
    content_block = BeautifulSoup(get(CURRENT_PETITIONS).text, 'lxml').find('div', {'id': 'content_container_227460_227460'})
    petitions_list = BeautifulSoup(get(content_block.find_all('ul')[1].find('a')['href']).text, 'lxml').find('div', {'id': 'content_container_946480'})
    petitions = []
    for petition in petitions_list.find_all('a')[1:]:
        _petition_title = petition.text
        _petition_url = petition['href']
        petitions.append({'title': _petition_title, 'url': _petition_url})
    return petitions