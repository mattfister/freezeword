"""
Provides access to a reduced, offline version of conceptnet. This uses a bunch of spliced up json files located
in the conceptnetreduced folder. Each time a request is made, the correct file is opened and the relations to the
concept are returned.
"""

__author__ = "Matt Fister"

import json
import os

# The number of json files that conceptnet has been split over
num_parts = 50


def string_hash(concept):
    """Returns the hashed number that corresponds to the json file that the concept is in."""
    sum = 0
    for i in range(len(concept)):
        sum += i*ord(concept[i])

    return sum % num_parts


def get_concept_relations(concept):
    """For the provided concept, return a list of relations that the concept has.

    The returned relations is of the form of a list of lists. Each of the inner lists is a pair of
    relations and concepts.

    E.G.
    get_concept_relations('avocado') returns
    [['HasA', 'skin'], ['IsA', 'fruit'], ... ['Synonym', 'alligator_pear']]
    """

    concept = concept.replace(' ', '_').lower()
    filename = 'conceptnet_reduced_en_' + str(string_hash(concept)) + '.json'
    with open(os.path.join(os.path.dirname(__file__), os.path.join('conceptnetreduced'), filename), 'r') as f:
        m = json.load(f)
        try:
            return m[concept]
        except KeyError:
            return []
    

if __name__ == '__main__':
    print(get_concept_relations('avocado'))
