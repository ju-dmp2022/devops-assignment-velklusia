from tests.test_base import BaseTestCalculator
import pytest

class TestCalculatorHelper(BaseTestCalculator):

    @pytest.mark.parametrize("a, b, expected", [
        (6, 3, 2),
        (-6, -3, 2),
        (3, -3, -1),
        (10, 2, 5),
    ])

    def test_divide(self, a, b, expected):
        # Act
        result = self.calculator.divide(a, b)

        # Assert
        assert result == expected

    @pytest.mark.parametrize("a, b", [
        (10, 0),
        (-5, 0),
    ])

    def test_divide_by_zero(self, a, b):
        # Act & Assert
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calculator.divide(a, b)

    @pytest.mark.parametrize("a, b, expected", [
        (3, 5, 8),
        (0, 0, 0),
        (-3, 3, 0),
        (-5, -5, -10),
    ])

    def test_add(self, a, b, expected):
        # Act
        result = self.calculator.add(a, b)

        # Assert
        assert result == expected

    @pytest.mark.parametrize("a, b, expected", [
        (10, 4, 6),
        (-3, -3, 0),
        (0, 0, 0),
        (-10, 5, -15),
    ])

    def test_subtract(self, a, b, expected):
        # Act
        result = self.calculator.subtract(a, b)

        # Assert
        assert result == expected

    @pytest.mark.parametrize("a, b, expected", [
        (6, 7, 42),
        (0, 5, 0),
        (-2, 3, -6),
        (-4, -5, 20),
    ])

    def test_multiply(self, a, b, expected):
        # Act
        result = self.calculator.multiply(a, b)

        # Assert
        assert result == expected
