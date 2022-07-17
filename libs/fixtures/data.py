import pytest

from libs.test_data.students_data import StudentData


@pytest.fixture
def student_data():
    return StudentData().return_data()
