import os
import random


class Dice:
    txts_path = os.path.dirname(os.path.abspath(__file__)) + os.sep + "ascii"

    def __init__(self) -> None:
        pass

    def get_dices_from_txt(self, file_name) -> dict:
        file_path = self.txts_path + os.sep + file_name
        dices = {}
        with open(file_path, "r") as file:
            lines = file.readlines()
            number = None
            for line in lines:
                if line.strip().isnumeric() or "3D" in line.strip():
                    number = line.strip()
                    dices[number] = ""
                    continue
                if number:
                    dices[number] = dices[number] + line
        return dices


class D6(Dice):
    file_name = "d6.txt"

    def __init__(self) -> None:
        super().__init__()
        dices = super().get_dices_from_txt(self.file_name)
        self.__set_dices(dices)

    def __set_dices(self, dices) -> None:
        self.one = dices.get("1")
        self.two = dices.get("2")
        self.three = dices.get("3")
        self.four = dices.get("4")
        self.five = dices.get("5")
        self.six = dices.get("6")
        self.three_d = dices.get("3D1")
        self.three_d_alt = dices.get("3D2")

    def roll(self) -> str:
        return random.choice([self.one, self.two, self.three, self.four, self.five, self.six])
