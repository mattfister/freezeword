""" Returns a list of words that rhyme with the desired word.
Uses cmudict from nltk.

Pronunciations use the first pronunciation in cmudict for each word.
"""

import nltk

__author__ = "Matt Fister"


def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


@memoize
def rhyme(inp):
    entries = nltk.corpus.cmudict.entries()
    syllables = [(word, syl) for word, syl in entries if word == inp]
    stress_index = 0
    print(syllables)
    if len(syllables) == 0:
        return {}
    for i, syllable in enumerate(syllables[0][1]):
        if '1' in syllable:
            stress_index = len(syllables[0][1])-i
    rhymes = []
    for (word, syllable) in syllables:
        for word2, pron in entries:
            if pron[-stress_index:] == syllable[-stress_index:]:
                rhymes += [word2]
    filteredRhymes = []
    for rhyme_word in rhymes:
        if len(nltk.corpus.wordnet.synsets(rhyme_word)) > 0 and inp != rhyme_word:
            filteredRhymes += [rhyme_word]
    return set(filteredRhymes)

if __name__ == "__main__":
    print(rhyme("banana"))
