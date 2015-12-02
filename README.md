# wordtools
This package contains some utility classes for various linguistic tasks. There are some vocabulary lists in the words folder. These can be accessed via wordLists or names. It also contains a reduced version of conceptnet that can be searched based on JSON representation located in the conceptnetreduced folder.

## Components

### conceptnet_reduced
**Overview**

An offline version of [conceptnet](http://conceptnet5.media.mit.edu/) is included in this package. This is a reduced version of conceptnet that removes all information except the map of concepts to other concepts via a relation. All non-English relations have been removed as well. This was done to make conceptnet consumable in an offline format, without relying on installing a huge database or requiring external dependencies.

In terms of underlying structure, the flattened concept data from conceptnet was split into the 50 json files in the conceptnetreduced folder to get under the github file size limit. When a concept is requested, the appropriate file is opened and its relations are returned. This supports reducing the memory footprint from loading all of conceptnet.

**Usage**

The method in concept_net_searcher called get_concept_relations returns a list of all relations concept pairs for the provided concept.

    from wordtools import conceptnet_searcher
    print conceptnet_searcher.get_concept_relations('avocado')

>[[u'HasA', u'skin'], [u'IsA', u'fruit'], [u'InstanceOf', u'specie'], [u'MemberOf', u'persea'], [u'HasProperty',     u'use_for_salad'], [u'InstanceOf', u'eukaryote'], [u'IsA', u'live_thing'], [u'IsA', u'oily_green_fruit'], [u'IsA', u'edible_fruit'], [u'RelatedTo', u'california_roll'], [u'RelatedTo', u'guacamole'], [u'RelatedTo', u'yellowish'], [u'RelatedTo', u'fruit'], [u'InstanceOf', u'plant'], [u'RelatedTo', u'green'], [u'Synonym', u'butter_pear'], [u'HasProperty', u'very_popular_in_vegetarian_cuisine'], [u'RelatedTo', u'green'], [u'RelatedTo', u'yellowish'], [u'HasA', u'more_protein_than_any_other_fruit'], [u'IsA', u'fruit_tree'], [u'PartOf', u'avocado'], [u'RelatedTo', u'laurel'], [u'RelatedTo', u'tree'], [u'IsA', u'greenery'], [u'PartOf', u'skin'], [u'RelatedTo', u'colour'], [u'Synonym', u'alligator_pear']]

### wordlists
**TODO**
### rhymes
**TODO**
