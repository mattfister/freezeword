__author__ = "Matt Fister"


def a_or_an(word):
    """Naively returns "a word" or "an word" depending on the word."""
    if len(word) > 0:
        if word[0] in 'aeiouAEIOU':
            return 'an'
        else:
            return 'a'
    else:
        return 'a'
