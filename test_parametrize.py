# import pytest
import calculator

calc = calculator.Calculator()


def test_add():
    first, second, expected = 1, 1, 2
    result = calc.add(first, second)
    assert result == expected

    first, second, expected = 2, 2, 4
    result = calc.add(first, second)
    assert result == expected

    first, second, expected = 4, 6, 10
    result = calc.add(first, second)
    assert result == expected

    first, second, expected = 5, 8, 13
    result = calc.add(first, second)
    assert result == expected

# @pytest.mark.parametrize(
#     "test_input, expected",
#     [('test_input_1', 'expected_1'),('test_input_2', 'expected_2')],
# )
