import pytest
import json
import aus_petitions.nt_parl

def test_nt_all():
    print(json.dumps(aus_petitions.nt_parl.all_petitions(), indent=2))