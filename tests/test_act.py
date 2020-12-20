import pytest, json, aus_petitions.act_parl

def test_act():
    print(aus_petitions.act_parl.all_petitions())
    print(str(len(json.loads(aus_petitions.act_parl.all_petitions()))) + ' petition(s) found.')