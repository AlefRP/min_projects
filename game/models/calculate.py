from typing import Union
from random import randint


class Calculate:
    def __init__(self: object, difficulty: int, /) -> None:
        self.__difficulty: int = difficulty
        self.__first_number: int = self._generate_number()
        self.__second_number: int = self._generate_number()
        self.__operation: int = self._set_operation()
        self.__result: int = self._generate_result()

    @property
    def difficulty(self: object) -> int:
        return self.__difficulty

    @property
    def first_number(self: object) -> int:
        return self.__first_number

    @property
    def second_number(self: object) -> int:
        return self.__second_number

    @property
    def operation(self: object) -> int:
        return self.__operation

    @property
    def result(self: object) -> int:
        return self.__result

    def __str__(self: object) -> str:
        op: str = ""
        match self.__operation:
            case 1:
                op = "+"
            case 2:
                op = "-"
            case 3:
                op = "*"
            case _:
                return "Unexpected operation"
        return f"{self.__first_number} {op} {self.__second_number} = {self.__result}"

    def _set_operation(self: object) -> int:
        return randint(1, 3)

    def _generate_number(self: object) -> Union[int, None]:
        if self.difficulty == 1:
            return randint(0, 10)
        elif self.difficulty == 2:
            return randint(0, 100)
        else:
            return randint(0, 1000)

    def _generate_result(self: object) -> int:
        match self.operation:
            case 1:
                return self.first_number + self.second_number
            case 2:
                return self.first_number - self.second_number
            case _:
                return self.first_number * self.second_number

    @property
    def _op_simbol(self: object) -> str:
        match self.operation:
            case 1:
                return "+"
            case 2:
                return "-"
            case _:
                return "*"

    def check_result(self: object, answer: int) -> bool:
        correct: bool = self.result == answer
        print("Correct!" if correct else "Incorrect!")
        print(
            f"{self.first_number} {self._op_simbol} {self.second_number} = {self.result}"
        )
        return correct

    def show_operation(self: object) -> None:
        print(f"{self.first_number} {self._op_simbol} {self.second_number} = ?")
