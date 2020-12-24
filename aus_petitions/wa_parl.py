from requests import get
from bs4 import BeautifulSoup
from .utils import format_methods

REQ_URL = ['https://www.parliament.wa.gov.au/parliament', '/commit.nsf/(viewPetitionsCurrent)']

def all_petitions():
    table = BeautifulSoup(get(REQ_URL[0] + REQ_URL[1], verify=False).text, 'lxml').find_all('tr')
    petition_list = []
    for row in table[1:]:
        row_entries = row.find_all('td')
        _petition_url = row.find('a')['href'].replace('..', REQ_URL[0])
        _petition_num = row.find('a').text
        _petition_date = format_methods.format_date(row_entries[1].text)
        _petition_signs = int(row_entries[2].text)
        _petition_subject = row_entries[3].text
        _petition_petitioner = row_entries[4].text
        _petition_tabler = row_entries[5].text
        status_split = row_entries[6].text.split(' ')
        _petition_status = status_split[0]
        _petition_status_date = format_methods.format_date(status_split[1])
        petition_list.append({'url': _petition_url, 'num': _petition_num, 'date': _petition_date, 'signatures': _petition_signs, 'title': _petition_subject, 'petitioner': _petition_petitioner, 'tabler': _petition_tabler, 'status': _petition_status, 'status_date': _petition_status_date})
    return petition_list

class wa_petition(object):
    def __init__(self, init_data):
        self.__init_data = init_data
        try:
            self.url = init_data['url']
            self.num = init_data['num']
            self.date = init_data['date']
            self.signatures = init_data['signatures']
            self.title = init_data['title']
            self.petitioner = init_data['petitioner']
            self.tabler = init_data['tabler']
            self.status = init_data['status']
            self.status_date = init_data['status_date']
            self.__petition_soup = BeautifulSoup(get(self.url, verify=False).text, 'lxml').find('div', {'id': 'tabs'})
        except:
            raise Exception('Input data must be a valid wa_petition dict.')
    
    @property
    def house(self):
        return self.__petition_soup.find('div', {'id': 'Details'}).find_all('tr')[1].find_all('td')[-1].text.strip()
    
    @property
    def committee(self):
        return self.__petition_soup.find('div', {'id': 'Details'}).find_all('tr')[0].find_all('td')[-1].text.strip()
    
    @property
    def pdf_url(self):
        return self.__petition_soup.find('div', {'id': 'Petitions'}).find('a', {'target': '_blank'})['href'].replace('/Parliament', REQ_URL[0])
    
    @property
    def data(self):
        return {
            **self.__init_data,
            'house': self.house,
            'committee': self.committee,
            'pdf_url': self.pdf_url
        }