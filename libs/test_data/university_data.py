import random
from dataclasses import asdict, dataclass, field

import requests
from faker import Faker


@dataclass
class UniversityData:
    resp = requests.get("http://worldtimeapi.org/api/timezone/")
    timezone = random.choice(resp.json())

    f = Faker(["en_US"])
    uni_name = " ".join(word.capitalize() for word in f.words(2))
    name: str = field(default=uni_name + " University")
    city: str = field(default=f.city())
    timezone: str = field(default=timezone)

    def return_data(self):
        return asdict(self)
