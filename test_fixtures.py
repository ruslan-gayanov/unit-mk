def test_multiplication(calculator):
    result = calculator.multiply(4, 3)
    assert result == 12


def test_division(calculator):
    result = calculator.divide(10, 2)
    assert result == 5
