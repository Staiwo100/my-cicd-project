import pytest
from src.calculator import add

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (100, -50, 50),
])
def test_add_cases(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.external
@pytest.mark.slow
def test_weather_api():
    # example placeholder
    assert True
