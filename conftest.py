import pytest
from calculator import Calculator


@pytest.fixture
def calculator():
    calc = Calculator()
    return calc
