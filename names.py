"""
Simple utility to get random names. I think it uses data from a US census, located in the words folder.
"""

__author__ = "Matt Fister"

import random
import os.path

maleFirsts = [line.rstrip('\n').title() for line in open(os.path.join(os.path.dirname(__file__), (os.path.join('words', 'maleFirstNames.txt'))))]
femaleFirsts = [line.rstrip('\n').title() for line in open(os.path.join(os.path.dirname(__file__), (os.path.join('words', 'femaleFirstNames.txt'))))]
lasts = [line.rstrip('\n').title() for line in open(os.path.join(os.path.dirname(__file__), (os.path.join('words', 'lastNames.txt'))))]


def get_first(gender):
    if gender == 'male':
        return random.choice(maleFirsts)
    else:
        return random.choice(femaleFirsts)


def get_last():
    return random.choice(lasts)


def get_name(gender):
    return get_first(gender) + " " + get_last()

if __name__ == "__main__":
    print(get_name(random.choice(['male', 'female'])))
