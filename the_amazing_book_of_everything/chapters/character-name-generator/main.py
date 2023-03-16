import random

from loguru import logger


def get_vowels() -> list:
    return ["a", "e", "i", "o", "u"]


def get_consonants() -> list:
    return [
        "b",
        "c",
        "d",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        "m",
        "n",
        "p",
        "q",
        "r",
        "s",
        "t",
        "v",
        "x",
        "w",
        "y",
        "z",
    ]


def is_vowels(letter: str) -> bool:
    return letter in get_vowels()


def is_consonant(letter: str) -> bool:
    return letter in get_consonants()


def get_letter(consonants=True, vowels=True) -> str:
    pass


if __name__ == "__main__":
    logger.info("Generating character name.")

    first_name_length = random.randint(3, 10)
    second_name_length = random.randint(3, 10)

    first_name = ""
    second_name = ""

    while len(first_name) < first_name_length:
        previous_letter = None

    for letter_position in range(0, first_name_length):
        previous_letter = None

        if previous_letter is None:
            alphabet = [get_vowels, get_consonants]
