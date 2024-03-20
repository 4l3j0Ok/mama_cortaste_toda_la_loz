from dices import D6
from time import sleep
import os
from colorama import Fore, Style


def main():
    clear()
    d6 = D6()
    drawn = d6.roll()
    animation(d6)
    print(f"{Fore.GREEN}Ha salido el siguiente dado: {Style.RESET_ALL}")
    print(drawn)


def animation(dice, delay=0.5, times=5, faces=6):
    title = f"{Fore.BLUE}Tirando un dado de {faces} caras...{Style.RESET_ALL}"
    for _ in range(times):
        print(title)
        print(dice.three_d)
        sleep(delay)
        clear()
        print(title)
        print(dice.three_d_alt)
        sleep(delay)
        clear()


def clear():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    main()
