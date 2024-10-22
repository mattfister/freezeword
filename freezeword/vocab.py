""" Provides access to the word lists located in the words folder.
"""

import random
import os.path
from freezeword import rhymes

__author__ = "Matt Fister"

adjs = [line.rstrip('\n') for line in open(os.path.join(os.path.dirname(__file__), (os.path.join('words', 'a.txt'))))]
nouns = [line.rstrip('\n') for line in open(os.path.join(os.path.dirname(__file__), (os.path.join('words', 'n.txt'))))]
verbs = [line.rstrip('\n') for line in open(os.path.join(os.path.dirname(__file__), (os.path.join('words', 'v.txt'))))]
living_things = [line.rstrip('\n') for line in open(os.path.join(os.path.dirname(__file__), (os.path.join('words', 'livingThings.txt'))))]
celebs = [line.rstrip('\n') for line in open(os.path.join(os.path.dirname(__file__), (os.path.join('words', 'celebs.txt'))))]
places = [line.rstrip('\n') for line in open(os.path.join(os.path.dirname(__file__), (os.path.join('words', 'places.txt'))))]
place_adjs = [line.rstrip('\n') for line in open(os.path.join(os.path.dirname(__file__), (os.path.join('words', 'placeAdjs.txt'))))]
ogden_basic_nouns = [line.rstrip('\n') for line in open(os.path.join(os.path.dirname(__file__), (os.path.join('words', 'ogdenBasicNouns.txt'))))]
living_thing_adjs = [line.rstrip('\n') for line in open(os.path.join(os.path.dirname(__file__), (os.path.join('words', 'livingThingAdjs.txt'))))]
fantasy_places = [line.rstrip('\n') for line in open(os.path.join(os.path.dirname(__file__), (os.path.join('words', 'fantasyPlaces.txt'))))]
ruin_rooms = [line.rstrip('\n') for line in open(os.path.join(os.path.dirname(__file__), (os.path.join('words', 'ruinRooms.txt'))))]
ruin_connectors = [line.rstrip('\n') for line in open(os.path.join(os.path.dirname(__file__), (os.path.join('words', 'ruinConnectors.txt'))))]
ruin_connector_adjs = [line.rstrip('\n') for line in open(os.path.join(os.path.dirname(__file__), (os.path.join('words', 'ruinConnectorAdjs.txt'))))]
fantasy_props = [line.rstrip('\n') for line in open(os.path.join(os.path.dirname(__file__), (os.path.join('words', 'fantasyProps.txt'))))]
fantasy_races = ['elf', 'orc', 'dwarf', 'golem', 'kobold', 'gnome']
fantasy_occupations = ['traders', 'soldiers', 'miners', 'settlers', 'wizards']
positive_qualities = [line.rstrip('\n') for line in open(os.path.join(os.path.dirname(__file__), (os.path.join('words', 'positiveQualities.txt'))))]
negative_qualities = [line.rstrip('\n') for line in open(os.path.join(os.path.dirname(__file__), (os.path.join('words', 'negativeQualities.txt'))))]
basic_colors = ["black", "gray", "pink", "white", "blue", "green", "purple", "yellow", "brown", "orange", "red"]
scents = [line.rstrip('\n') for line in open(os.path.join(os.path.dirname(__file__), (os.path.join('words', 'scents.txt'))))]

def get_noun():
    return random.choice(nouns).replace("_", " ")


def get_adj():
    return random.choice(adjs)


def get_celeb():
    return random.choice(celebs)


def get_living_thing():
    return random.choice(living_things)


def get_place():
    return random.choice(places)


def get_place_adj():
    return random.choice(place_adjs)


def get_fantasy_place():
    return random.choice(fantasy_places)


def get_ogden_basic_noun():
    return random.choice(ogden_basic_nouns)


def get_living_thing_adj():
    return random.choice(living_thing_adjs)


def get_fantasy_prop():
    return random.choice(fantasy_props)


def get_fantasy_race():
    return random.choice(fantasy_races)


def get_fantasy_occupation():
    return random.choice(fantasy_occupations)


def get_positive_quality():
    return random.choice(positive_qualities)


def get_negative_quality():
    return random.choice(negative_qualities)


def get_ruin_room():
    return random.choice(ruin_rooms)


def get_ruin_connector():
    return random.choice(ruin_connectors)


def get_ruin_connector_adj():
    return random.choice(ruin_connector_adjs)


def get_basic_color():
    return random.choice(basic_colors)


def get_scent():
    return random.choice(scents)


def rhyming_adjs(word):
    all_rhymes = rhymes.rhyme(word)
    rhyming_adjs = []
    for rhyme in all_rhymes:
        if rhyme in adjs:
            rhyming_adjs.append(rhyme)
    return rhyming_adjs


def rhyming_nouns(word):
    all_rhymes = rhymes.rhyme(word)
    rhyming_nouns = []
    for rhyme in all_rhymes:
        if rhyme in nouns:
            rhyming_nouns.append(rhyme)
    return rhyming_nouns

if __name__ == "__main__":
    print(get_noun())
    print(get_adj())
    print(get_celeb())
    print(get_living_thing())
    print(get_place())
    print(get_ruin_room())
    print(rhyming_adjs('shot'))
    print(rhyming_nouns('truth'))

