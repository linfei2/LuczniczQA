import random
from dataclasses import asdict, dataclass, field

from faker import Faker


@dataclass
class StudentData:
    random_year = random.randrange(1, 6)
    random_gpa = round(random.uniform(1.0, 5.0), 2)
    random_major = random.choice(
        ["Physics", "Computer Science", "Biology", "Law", "Medicine", "Literature"]
    )

    f = Faker("en_US")
    fullname: str = field(default=f.name())
    email: str = field(default=f.free_email())
    course_of_study: str = field(default=random_major)
    year: int = field(default=random_year)
    gpa: str = field(default=random_gpa)

    def return_data(self):
        return asdict(self)
