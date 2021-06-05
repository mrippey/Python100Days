import pathlib 
from dataclasses import dataclass
from dataclass_csv import DataclassReader 
from typing import List
from collections import Counter

data = []

@dataclass
class Tickets:
    Event: str
    Division: str
    AvgTP: float


def setup_csv_stuff():
    base_file = pathlib.Path(__file__).resolve().parent
    filename = pathlib.Path.joinpath(base_file, 'data', 'nfl_tickets.csv')

    with open(filename, 'r', encoding='utf-8')as file_out:
        text = DataclassReader(file_out, Tickets)

        for rows in text:         
            data.append(rows)


def most_expensive() -> List[Tickets]:
    return sorted(data, key=lambda r: -r.AvgTP)

def least_expensive() -> List[Tickets]:
    return sorted(data, key=lambda r: r.AvgTP)

# Big thank you to David from the PyBites Slack for assisting me with parsing the Division column
def division_appearances() -> List[Tickets]:
   print(Counter(t.Division for t in data))
