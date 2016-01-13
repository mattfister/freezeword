__author__ = "Matt Fister"


def he_or_she(word):
    """Returns he or she depending on if the word is 'male' or 'female'.
    :param word: 'male', 'female' or anything else
    """
    if word == 'male':
        return 'he'
    elif word == 'female':
        return 'she'
    else:
        return 'it'


def him_or_her(word):
    """Returns him or her depending on if the word is 'male' or 'female'.
    :param word: 'male', 'female' or anything else
    """
    if word == 'male':
        return 'him'
    elif word == 'female':
        return 'her'
    else:
        return 'its'
