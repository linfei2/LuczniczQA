import pytest

from libs.test_data.students_data import StudentData
from libs.test_data.university_data import UniversityData


@pytest.fixture
def student_data():
    return StudentData().return_data()


@pytest.fixture
def university_data():
    return UniversityData().return_data()
