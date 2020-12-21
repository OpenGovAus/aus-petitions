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
        return petition_list
    else:
        return []

class act_petition(object):
    def __init__(self, init_data):
        try:
            self.url = init_data['url']
            self.title = init_data['title']
            self.num = init_data['num']
            self.closing_date = init_data['date']
            try:
                self.petition_soup = BeautifulSoup(get(self.url).text, 'lxml')
            except:
                raise Exception('Could not scrape petition page.')
        except:
            raise Exception('Input data must be a valid act_petition dict.\n' + str(init_data))
    
    @property
    def eligibility(self):
        return self.__get_property_text('Eligibility:')
    
    @property
    def sponsor(self):
        return self.__get_property_text('Sponsoring Member:')

    @property
    def petitioner(self):
        return self.__get_property_text('Principal Petitioner:')
    
    @property
    def signature_total(self):
        try:
            return int(self.__get_property_text('Number of Signatures:'))
        except:
            return None
        
    @property
    def post_date(self):
        return format_methods.format_date(self.__get_property_text('Posting Date:'))
    
    @property
    def petition_text(self):
        return self.petition_soup.find('span', {'id': 'ctl00_ContentPlaceHolder1_DetailsView2_lblDescription'}).text.strip()

    def __get_property_text(self, prop_title):
        return self.petition_soup.find('b', text=prop_title).findNext('td').text.strip()

    @property
    def data(self):
        return {
            'url': self.url,
            'num': self.num,
            'title': self.title,
            'post_date': self.post_date,
            'closing_date': self.closing_date,
            'sponsor': self.sponsor,
            'eligibility': self.eligibility,
            'petitioner': self.petitioner,
            'signature_total': self.signature_total,
            'petition_text': self.petition_text.replace('\t', '').replace('\r-', ' ').replace('\r', '').replace('\u2019', '\'')
        }