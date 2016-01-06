""" Returns a list of words that rhyme with the desired word.
Uses cmudict from nltk.

Rhyming is complicated and I haven't quite figured it out yet... :(

But it sort of works.
"""

import nltk

__author__ = "Matt Fister"


def rhyme(inp):
    entries = nltk.corpus.cmudict.entries()
    syllables = [(word, syl) for word, syl in entries if word == inp]
    minlength = len(syllables)
    rhymes = []
    for (word, syllable) in syllables:
        for word2, pron in entries:
            if pron[-2:] == syllable[-2:]:
                rhymes += [word2]
    filteredRhymes = []
    for rhyme in rhymes:
        if len(nltk.corpus.wordnet.synsets(rhyme)) > 0 \
                and not rhyme in inp and not inp in rhyme:
            filteredRhymes += [rhyme]
    return set(filteredRhymes)

if __name__ == "__main__":
    print(rhyme("banana"))
