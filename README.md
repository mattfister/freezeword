# freezeword
![freezeword logo](http://freezebeam.com/wp-content/uploads/2015/12/Drawing.png)

This package contains some utility classes for various linguistic tasks. There are some vocabulary lists in the words folder. These can be accessed via vocab or names. It also contains a reduced version of conceptnet that can be searched based on JSON representation located in the conceptnetreduced folder.

---

## Components

### conceptnet_reduced
**Overview**

An offline version of [conceptnet](http://conceptnet5.media.mit.edu/) is included in this package. This is a reduced version of conceptnet that removes all information except the map of concepts to other concepts via a relation. All non-English relations have been removed as well. This was done to make conceptnet consumable in an offline format, without relying on installing a huge database or requiring external dependencies.

In terms of underlying structure, the flattened concept data from conceptnet was split into the 50 json files in the conceptnetreduced folder to get under the github file size limit. When a concept is requested, the appropriate file is opened and its relations are returned. This supports reducing the memory footprint from loading all of conceptnet.

**Usage**

The method in concept_net_searcher called get_concept_relations returns a list of all relations concept pairs for the provided concept.

```python
print(conceptnet_searcher.get_concept_relations('avocado'))

[[u'HasA', u'skin'], [u'IsA', u'fruit'], [u'InstanceOf', u'specie'], [u'MemberOf', u'persea'],
[u'HasProperty',     u'use_for_salad'], [u'InstanceOf', u'eukaryote'], [u'IsA', u'live_thing'],
[u'IsA', u'oily_green_fruit'], [u'IsA', u'edible_fruit'], [u'RelatedTo', u'california_roll'],
[u'RelatedTo', u'guacamole'], [u'RelatedTo', u'yellowish'], [u'RelatedTo', u'fruit'],
[u'InstanceOf', u'plant'], [u'RelatedTo', u'green'], [u'Synonym', u'butter_pear'],
[u'HasProperty', u'very_popular_in_vegetarian_cuisine'], [u'RelatedTo', u'green'],
[u'RelatedTo', u'yellowish'], [u'HasA', u'more_protein_than_any_other_fruit'],
[u'IsA', u'fruit_tree'], [u'PartOf', u'avocado'], [u'RelatedTo', u'laurel'],
[u'RelatedTo', u'tree'], [u'IsA', u'greenery'], [u'PartOf', u'skin'],
[u'RelatedTo', u'colour'], [u'Synonym', u'alligator_pear']]
```

---

### md_writer
**TODO**

---

### names
**Overview**

Simple utility to get random names. Names are US Centric since they are based on census data.

**Usage**

```python
print(names.get_name('female'))

Jeana Gilliam
```

---

### num_to_words
**Overview**

Converts numbers to their spelled out English description.

**Usage**

```python
print(num_to_words.num_to_words(53270))

fifty three thousand, two hundred seventy
```

---

### old_language_generator
**Overview**

Translates words to a nonsensical "ancient" language via letter replacement.

**Usage**

```python
print(old_language_generator.translate_word("Hello world"))

Hahhu iaufhl
````

---

### rhymes
**TODO**

---

### templates
**Overview**

A templating library for resolving sentence templates. Iteratively processes until all recursive variable substitution is evaluated.

**Usage**

*Syntax*

Variables are represented by {{variable name}}. Random choices can be provided to variables either as lists or strings separated by the | symbol. One of the choices will be selected for evaluation.

*Example*

```python
context = {'greeting': ['bonjour'.title(), 'hello'.title(), 'yo'.title()], 'world': '{{adjective}} world',
           'adjective': '{{sad word}}|{{happy word}}',
           'sad word': 'crappy|sad', 'happy word': 'joyful|crazy|wonderful'}
print(Template("{{greeting}} {{world}}").render(**context))

Hello crazy world

print(Template("{{greeting}} {{world}}").render(**context))

Bonjour sad world
```

---

### vocab
**Overview**

Provides access to the word lists located in the words folder.

**Usage**

```python
print(vocab.get_living_thing())

pioneer
```

---

### word_tests
**TODO**

---

###
Credits:
Ice graphic by <a href="http://www.freepik.com/">Freepik</a> from <a href="http://www.flaticon.com/">Flaticon</a> is licensed under <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0">CC BY 3.0</a>. Made with <a href="http://logomakr.com" title="Logo Maker">Logo Maker</a>

---
