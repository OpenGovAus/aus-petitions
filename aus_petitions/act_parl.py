import json
from requests import get
from bs4 import BeautifulSoup
from .utils import format_methods

CURRENT_PETITIONS = 'https://epetitions.act.gov.au/CurrentEPetitions.aspx'

def all_petitions():
    petition_list = []
    try:
        petitions = BeautifulSoup(get(CURRENT_PETITIONS).text, 'lxml').find('table', {'id': 'ctl00_ContentPlaceHolder1_GridView1'}).find_all('tr')[1:]
    except:
        raise Exception('Could not find ACT petitions HTML table.')
    
    if petitions:
        for petition in petitions:
                _petition_num = petition.find('td').text
                _petition_title = petition.find('a').text
                _petition_url = petition.find('a')['href']
                _petition_date = format_methods.format_date(petition.find_all('td')[-1].text)
                petition_list.append({'num': _petition_num, 'title': _petition_title, 'url': 'https://epetitions.act.gov.au/' + _petition_url, 'date': _petition_date})
        return json.dumps(petition_list, indent=2)
    else:
        return json.dumps({}, indent=2)

class act_petition(object):
    def __init__(self):
        pass