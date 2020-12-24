# aus-petitions

A Python package to obtain current petitions from the various Australian parliaments.

#### Currently Supported Parliaments

- ACT
- NT
- WA

## Installation

Install dependencies with **pip3**:

```sh
pip3 install -r requirements.txt
```

## Usage

Import desired parliament module:

```python
import aus_petitions.act_parl
```

#### Return all petitions:

```python
import json

print(json.dumps(aus_petitions.act_parl.all_petitions()))
```

Prints out something like this:

```sh
[
  {
    "num": "025-20",
    "title": "Improve and strengthen drug and alcohol treatment services in Canberra",
    "url": "https://epetitions.act.gov.au/CurrentEPetition.aspx?PetId=157&lIndex=-1",
    "date": "07-02-2021 "
  }
]
```

#### Return more data for a petition

```python
import random, json

random_petition = random.choice(aus_petitions.act_parl.all_petitions())
more_data = aus_petitions.act_parl.act_petition(random_petition)

print(json.dumps(more_data.data, indent=2))
```

Prints out:

```json
{
  "url": "https://epetitions.act.gov.au/CurrentEPetition.aspx?PetId=157&lIndex=-1",
  "num": "025-20",
  "title": "Improve and strengthen drug and alcohol treatment services in Canberra",
  "post_date": "07-12-2020",
  "closing_date": "07-02-2021 ",
  "sponsor": "Mrs Elizabeth Kikkert",
  "eligibility": "Residents of ACT",
  "petitioner": "Mary Bingham",
  "signature_total": 82,
  "petition_text": "The following residents of the ACT draw to the attention of the Assembly that: according to ACIC reporting, the average consumption of many major drugs, including alcohol and tobacco, has been increasing in the ACT in recent years; specialist alcohol, tobacco and other drug services in the territory can no longer meet demand, with waiting lists growing even longer in 2020; delays in accessing rehabilitation services may negatively hinder successful treatment; and research confirms the link between alcohol and other drugs and violence in the home. The petitioners, therefore, request the Assembly to call upon ACT Government to conduct a thorough inquiry into the alcohol, tobacco and other drug service sector, including prevention/early intervention services and pathways as well as treatment/rehabilitation services, both for persons on Drug and Alcohol Treatment Orders and those voluntarily seeking help, to: identity current strength and weaknesses; access current and future demands; and recommend service and funding models that will better meet people's needs."
}
```

# Contributing

To add a parliament, fork this repo and create a file called `jurisdiction_parl.py` (e.g `nt_parl.py`, `sa_parl.py`, etc).

In it, create a method called `all_petitions()`. This function should return data listed on the parliament's home petitions website in a Python `list`.

Also create a `class` called `jurisdiction_petition(object)` (e.g `act_petition(object)`, `nt_petition(object)`, etc). This `class` should contain properties with all the data from the individual bill's web page. It should also have a property called `data` which returns a `dict` of all the other properties in the class.

---

When done, [create a Pull Request](https://github.com/OpenGovAus/aus-petitions/compare) and your code will be reviewed, then probably merged.