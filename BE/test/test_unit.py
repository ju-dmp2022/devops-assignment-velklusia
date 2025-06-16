import pytest
from assertpy import assert_that
from test_base import BaseTestCalculator

class TestCalculator(BaseTestCalculator):
    
    #
    # UNIT TESTING
    #
    
    def test_add(self):
        # Arrange
        a, b = 1, 2
        # Act
        result = self.calculator.add(a, b)
        # Assert
        assert_that(result).is_equal_to(3)

    def test_subtract(self):
        # Arrange
        a, b = 1, 2
        # Act
        result = self.calculator.subtract(a, b)
        # Assert
        assert_that(result).is_equal_to(-1)

    def test_multiply(self):
        # Arrange
        a, b = 2, 3
        # Act
        result = self.calculator.multiply(a, b)
        # Assert
        assert_that(result).is_equal_to(6)

    def test_divide(self):
        # Arrange
        a, b = 6, 3
        # Act
        result = self.calculator.divide(a, b)
        # Assert
        assert_that(result).is_equal_to(2)

    def test_divide_by_zero(self):
        # Arrange
        a, b = 6, 0
        # Act & Assert
        with pytest.raises(ValueError):  # Expect ValueError instead of ZeroDivisionError
            self.calculator.divide(6, 0)
            
    #
    # DATA DRIVEN TESTING
    #
           
    @pytest.mark.parametrize("a, b, expected", [
        (1, 2, 3),
        (3, -3, 0),
        (0, 0, 0),
        (-1, -1, -2)
    ])
    def test_add(self, a, b, expected):
        result = self.calculator.add(a, b)
        assert_that(result).is_equal_to(expected)

    @pytest.mark.parametrize("a, b, expected", [
        (1, 2, -1),
        (3, -3, 6),
        (0, 0, 0),
        (-1, -1, 0)
    ])
    def test_subtract(self, a, b, expected):
        result = self.calculator.subtract(a, b)
        assert_that(result).is_equal_to(expected)

    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 6),
        (3, -3, -9),
        (0, 1, 0),
        (-1, -1, 1)
    ])
    def test_multiply(self, a, b, expected):
        result = self.calculator.multiply(a, b)
        assert_that(result).is_equal_to(expected)

    @pytest.mark.parametrize("a, b, expected", [
        (6, 3, 2),
        (-6, -3, 2),
        (3, -3, -1)
    ])
    def test_divide(self, a, b, expected):
        result = self.calculator.divide(a, b)
        assert_that(result).is_equal_to(expected)