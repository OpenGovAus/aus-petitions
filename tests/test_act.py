import pytest, json, aus_petitions.act_parl, random

def test_act():
    print(json.dumps(aus_petitions.act_parl.all_petitions(), indent=2))
    print(str(len(aus_petitions.act_parl.all_petitions())) + ' petition(s) found.')

def test_act_class():
    print(json.dumps(aus_petitions.act_parl.act_petition(random.choice(aus_petitions.act_parl.all_petitions())).data, indent=2))