from enum import Enum


class Opertions(str, Enum):
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"

    def __str__(self) -> str:
        return str(self.value)
