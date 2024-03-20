from enum import Enum
import os


class Dices:
    txts_path = "./dices"

    def __init__(self) -> None:
        pass

    def get_dices(self, file_name):
        file_path = self.txts_path + os.sep + file_name
        with open(file_path, "r") as file:
            lines = file.readlines()
            number = None
            for line in lines:
                if line.strip().isnumeric():
                    number = line.strip()
                    setattr(self, number, "")
                    continue
                if number:
                    setattr(self, number, getattr(self, number) + line)


class D6(Dices):
    file_name = "d6.txt"

    def __init__(self) -> None:
        super().__init__()
        super().get_dices(self.file_name)
        self.__set_dices()

    def __set_dices(self):
        self.one = self.__getattribute__("1")
        self.__delattr__("1")
        self.two = self.__getattribute__("2")
        self.__delattr__("2")
        self.three = self.__getattribute__("3")
        self.__delattr__("3")
        self.four = self.__getattribute__("4")
        self.__delattr__("4")
        self.five = self.__getattribute__("5")
        self.__delattr__("5")
        self.six = self.__getattribute__("6")
        self.__delattr__("6")


print(D6().__dict__)