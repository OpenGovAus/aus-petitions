from requests import get
import json

def all_petitions():
    petitions = []
    petition_json = json.loads(get('https://epetitions.aph.gov.au/petitions/all').text)
    for raw_petition in petition_json:
        data_dict = {
            'id': raw_petition['Petition_Id'],
            'num': raw_petition['PetitionNumber'],
            'reason': raw_petition['PetitionReason'],
            'title': raw_petition['PetitionTitle'],
            'petitioner': raw_petition['PPetitionerName'],
            'signatures': raw_petition['SignatureCount'],
            'request_date': raw_petition['RequestDate'],
            'present_date': raw_petition['Presented_Date'],
            'is_refered': raw_petition['isRefered'],
            'refered_date': raw_petition['Referred_Date'],
            'is_responded': raw_petition['isResponded'],
            'response_date': raw_petition['Responded_Date'],
            'response_content': raw_petition['Response_Content'],
            'closing_date': raw_petition['SignDeadline'],
            'petitioned_to': raw_petition['PetitionAddress'],
            'petition_of': raw_petition['PetitionOf'],
            'text': raw_petition['PetitionRequest'],
            'is_paper': raw_petition['IsPaperPetition'],
        }
        
        if(data_dict['is_responded']):
            data_dict['response_content'] = 'https://epetitions.aph.gov.au/MResponse/get?id=%s' % (data_dict['num'])
        
        petitions.append(data_dict)
    return petitions

class fed_petition(object):
    def __init__(self, init_data):
        self.data = init_data
        self.id = init_data['id']
        self.num = init_data['num']
        self.reason = init_data['reason']
        self.title = init_data['title']
        self.petitioner =  init_data['petitioner']
        self.signatures = init_data['signatures']
        self.request_date = init_data['request_date']
        self.present_date = init_data['present_date']
        self.is_refered = init_data['is_refered'],
        self.refered_date = init_data['refered_date']
        self.is_responded = init_data['is_responded']
        self.response_date = init_data['response_date']
        self.response_content = init_data['response_content']
        self.closing_date = init_data['closing_date']
        self.petitioned_to = init_data['petitioned_to']
        self.petition_of = init_data['petition_of']
        self.text = init_data['text']
        self.is_paper = init_data['is_paper']