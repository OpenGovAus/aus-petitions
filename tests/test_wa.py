import pytest, json, random
import aus_petitions.wa_parl

def test_wa_all():
    print(json.dumps(aus_petitions.wa_parl.all_petitions(), indent=2))

def test_wa_single():
    petition = aus_petitions.wa_parl.wa_petition(random.choice(aus_petitions.wa_parl.all_petitions()))
    print(json.dumps(petition.data, indent=2))