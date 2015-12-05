"""
Inspired by https://github.com/aparrish/nanogenmo2015/blob/master/extract.py,
this has some methods to determine if certain words are a kind of thing,
for instance a disco is a place, and so is a cemetery, but an avocado is not.

This is dependent on nltk's wordnet implementation
"""

from nltk.corpus import wordnet


def recursive_hypernyms(synset, all_hypernyms):
    hypernyms = synset.hypernyms()
    for hypernym in hypernyms:
        all_hypernyms.append(hypernym)
        recursive_hypernyms(hypernym, all_hypernyms)
    return all_hypernyms


def all_hypernyms(word):
    synsets = wordnet.synsets(word)
    hypernyms = []
    for synset in synsets:
        hypernyms += recursive_hypernyms(synset, [])
    return hypernyms


def is_a(word, synset):
    hypernyms = all_hypernyms(word)
    for hypernym in hypernyms:
        if synset == hypernym.name():
            return True
    return False


def is_one_of(word, synsets):
    for synset in synsets:
        if is_a(word, synset):
            return True
    return False

def is_place(word):
    place_synsets = ['area.n.05', 'structure.n.01', 'geological_formation.n.01', 'region.n.03',
                     'location.n.01']
    return is_one_of(word, place_synsets)

if __name__ == '__main__':
    print(all_hypernyms('disco'))
    print(is_place('disco'))
    print(is_place('avocado'))
    print(all_hypernyms('cemetery'))
    print(is_place('cemetery'))
    print(all_hypernyms('mountain'))
    print(is_place('mountain'))
