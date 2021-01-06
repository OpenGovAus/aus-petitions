import pytest, json
import aus_petitions.fed_parl

def test_fed(): # All data is grabbed through all_petitions, so there's no point testing the same values twice.
    print(json.dumps(aus_petitions.fed_parl.all_petitions(), indent=2))
    print(str(len(aus_petitions.fed_parl.all_petitions())) + ' petition(s) found.')