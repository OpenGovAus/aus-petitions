# aus-petitions

A Python package to obtain current petitions from the various Australian parliaments.

#### Currently Supported Parliaments

- ACT

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

Return all petitions:

```python
print(aus_petitions.act_parl.all_petitions())
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