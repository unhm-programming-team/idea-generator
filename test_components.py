"""
For testing sentence_components.py
"""

from sentence_components import *

testComponent = Component('pre-',['num1','num2','num3'], ['next'])

print(testComponent.get_a_descriptor(1))
assert (testComponent.get_a_descriptor(0) == 'pre- num1'), "Component returning wrong next!"
assert (testComponent.get_a_descriptor(1) == 'pre- num2'), "Component returning wrong next!"
assert (testComponent.get_a_descriptor(2) == 'pre- num3'), "Component returning wrong next!"
assert (testComponent.get_a_descriptor(3) == 'pre- num1'), "Component returning wrong next!"
assert (testComponent.get_a_descriptor(4) == 'pre- num2'), "Component returning wrong next!"
assert (testComponent.get_a_descriptor(5) == 'pre- num3'), "Component returning wrong next!"
assert (testComponent.get_a_descriptor(6) == 'pre- num1'), "Component returning wrong next!"
assert (testComponent.get_a_descriptor(7) == 'pre- num2'), "Component returning wrong next!"
assert (testComponent.get_a_descriptor(8) == 'pre- num3'), "Component returning wrong next!"
assert (testComponent.get_a_descriptor(9) == 'pre- num1'), "Component returning wrong next!"


goalTarget = ComponentRegistry.registry['goal_target']
assert(goalTarget.get_next_type(5) == 'bad_guy_interaction'), "Bad guy comes after goal type in registry"
assert(goalTarget.get_a_descriptor(4) == 'your sunglasses'), "Descriptor not as expected"

x = ArticleAdjectiveComponent.split_on_article('a firefighter')

assert(ArticleAdjectiveComponent.split_on_article('a firefighter') == ('a','firefighter')), "Articles not splitting"
assert(ArticleAdjectiveComponent.split_on_article('an astronaut') == ('an','astronaut')), "Articles not splitting"
assert(ArticleAdjectiveComponent.split_on_article('a wild boar') == ('a','wild boar')), "Articles not splitting"

test_adj = ArticleAdjectiveComponent('',['fly'],['a human'],['none'])
print(test_adj.get_a_descriptor(1))

test_sentence = ComponentRegistry.get_traversed_sentence(55)
print(test_sentence)
test_sentence = ComponentRegistry.get_traversed_sentence(100)
print(test_sentence)