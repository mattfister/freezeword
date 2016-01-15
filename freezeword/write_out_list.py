""" Given a list of objects, uses the str method to represent it as "a [0].str(), a [1].str(), and a [2].str()".
"""
import random
from freezeword import a_or_an
from freezeword import num_to_words

__author__ = "Matt Fister"


def write_out_list(list, shuffle):
    """
    :param list: The list to iterate over
    :param shuffle: True if the list should be shuffled prior to listing
    :return: a phrase shuch as "a list[0], and list[1], and twelve list[2]." Or [a list[1] and a list[2]
    """
    list_phrase = ""
    if shuffle:
        random.shuffle(list)
    if len(list) == 2:
        list_phrase += a_or_an.a_or_an(list[0].__str__()) + " " + list[0].__str__() + " and " + a_or_an.a_or_an(list[1].__str__()) + " " + list[1].__str__()
    else:
        for i in range(len(list)):
            list_phrase += a_or_an.a_or_an(list[i].__str__()) + " " + list[i].__str__()
            if i < len(list) - 2:
                list_phrase += ', '
            elif i == len(list) - 2:
                list_phrase += ', and '
    return list_phrase


def write_out_list_and_collect(list, shuffle):
    """
    :param list: The list to iterate over
    :param shuffle: True if the list should be shuffled prior to listing
    :return: a phrase shuch as "two list[0], a list[1], and twenty-eight list[2]." Or [a list[1] and a list[2]
    """
    list_phrase = ""

    collected = {}
    for thing in list:
        if thing in collected.keys():
            collected[thing] += 1
        else:
            collected[thing] = 1

    if len(collected.keys()) == 1:
        for i, (key, value) in enumerate(collected.items()):
            if value > 1:
                number = num_to_words.num_to_words(value)
                name = key.name_plural
            else:
                number = a_or_an.a_or_an(key.name)
                name = key.name
            list_phrase = number + " " + name
    elif len(collected.keys()) == 2:
        for i, (key, value) in enumerate(collected.items()):
            if value > 1:
                number = num_to_words.num_to_words(value)
                name = key.name_plural
            else:
                number = a_or_an.a_or_an(key.name)
                name = key.name
            if i == 0:
                list_phrase = number + " " + name + " and "
            else:
                list_phrase += number + " " + name

    else:
        for i, (key, value) in enumerate(collected.items()):
            if value > 1:
                number = num_to_words.num_to_words(value)
                name = key.name_plural
            else:
                number = a_or_an.a_or_an(key.name)
                name = key.name
            list_phrase += number + " " + name
            if i < len(list) - 2:
                list_phrase += ', '
            elif i == len(list) - 2:
                list_phrase += ', and '
    return list_phrase