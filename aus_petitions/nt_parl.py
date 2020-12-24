import re
from requests import get
from bs4 import BeautifulSoup

CURRENT_PETITIONS = 'https://parliament.nt.gov.au/business/petitions-and-responses'

def all_petitions():
    content_block = BeautifulSoup(get(CURRENT_PETITIONS).text, 'lxml').find('div', {'id': 'content_container_227460_227460'})
    petitions_list = BeautifulSoup(get(content_block.find_all('ul')[1].find('a')['href']).text, 'lxml').find('div', {'id': 'content_container_946480'})
    petitions = []
    for petition in petitions_list.find_all('a')[1:]:
        split_str = re.split(r' - ', petition.text)
        _petition_title = split_str[1].strip()
        _petition_number = split_str[0].replace('Petition ', '').strip()
        _petition_url = petition['href']
        petitions.append({'title': _petition_title, 'url': _petition_url, 'num': _petition_number})
    return petitions