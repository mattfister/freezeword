""" Given a list of objects, uses the str method to represent it as "[0].str(), [1].str(), and [2].str()".
"""
import random


__author__ = "Matt Fister"


def write_out_list(list, shuffle):
    """
    :param list: The list to iterate over
    :param shuffle: True if the list should be shuffled prior to listing
    :return: a phrase shuch as "list[0], list[1], and list[1]." Or [list[1] and list[2]
    """
    list_phrase = ""
    if shuffle:
        random.shuffle(list)
    if len(list) == 2:
        list_phrase += list[0].__str__() + " " + list[1].__str__()
    else:
        for i in range(len(list)):
            list_phrase += list[i].__str__()
            if i < len(list) - 2:
                list_phrase += ', '
            elif i == len(list) - 2:
                list_phrase += ', and '
    return list_phrase
