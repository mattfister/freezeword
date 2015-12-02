import json
import sys
import os

# The number of json files that conceptnet is split over
num_parts = 50


def string_hash(concept):
    """Returns the hashed number that corresponds to the json file that the concept is in"""
    sum = 0
    for i in range(len(concept)):
        sum += i*ord(concept[i])

    return sum % num_parts


def get_concept_relations(concept):
    """For the provided concept, return a list of relations that the concept has"""
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
