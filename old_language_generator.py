from vocab import WordLists

words = WordLists()


def translate_word(word):
    new_word = ""
    letter_map = {'a': 'e', 'b': 'd', 'c': 'c', 'd': 'l', 'e': 'a', 'f': 'g', 'g': 'h', 'h': 'm',
                  'i': 'ae', 'j': 'c', 'k': 'c', 'l': 'h', 'm': 'b', 'n': 'm', 'o': 'u', 'p': 'd', 'q': 'c',
                  'r': 'f', 's': 'i', 't': 'd', 'u': 'o', 'v': 'u', 'w': 'ia', 'x': 's', 'y': 'wi', 'z': 's'}
    for letter in word:
        try:
            new_word += letter_map[letter]
        except KeyError:
            new_word += letter

    return new_word


def random_word():
    return translate_word(words.get_noun())


if __name__ == '__main__':
    print(random_word())
