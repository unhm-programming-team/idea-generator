"""
Sentence Components

rough draft just to make something work
"""
from data import Data
import random

class Component:
    """
    Components contain a list of possible descriptor strings, such as:
    ['an astronaut', 'a firefighter']
    They contain a list of strings corresponding to next Components available in the Component registry.
    The next Component will be called to build the sentence.
    ['origin']
    """
    def __init__(self, prepend_word, descriptors, next_types, append_word = ''):
        self.descriptors = descriptors
        self.next_types = next_types
        self.prepend_word = prepend_word
        self.append_word = append_word

    def get_a_descriptor(self, num=0):
        return f"{self.prepend_word} {Component.get_normalized(num, self.descriptors)} {self.append_word}".strip()

    def get_next_type(self, num=0):
        return Component.get_normalized(num, self.next_types)

    @staticmethod
    def get_normalized(num, string_array):
        """
        Called by getters so numbers beyond list bounds will still return values
        :param num:
        :param string_array:
        :return:
        """
        list_length = len(string_array)
        if num == 0:
            if list_length < 1:
                return 'none'
            else:
                return string_array[0]
        return string_array[int(num % list_length)]


class ArticleAdjectiveComponent(Component):
    def __init__(self, prepend_word, adjectives, descriptors, next_types, append_word=''):
        """
        Puts an adjective between article and noun
        :param descriptors:
        :type descriptors: list<str>
        :param next_types: correspond to registry dictionary entries
        :type next_types: list<str>
        :param adjectives:
        :type adjectives: list<str>
        :param prepend_word:
        :type prepend_word: str
        :param append_word:
        :type append_word: str
        """
        Component.__init__(self, prepend_word, descriptors, next_types, append_word)
        self.adjectives = adjectives

    def get_a_descriptor(self, num=0):
        descriptor_pair = ArticleAdjectiveComponent.split_on_article(Component.get_normalized(num, self.descriptors))
        adjective = Component.get_normalized(num, self.adjectives)  # passing the same seed might make it too repetitive
        return f"{self.prepend_word} {descriptor_pair[0]} {adjective} {descriptor_pair[1]} {self.append_word}".strip()

    @staticmethod
    def split_on_article(descriptor):
        splits = descriptor.split(' ')
        front = splits[0]
        back = ' '.join(splits[1:])
        return front, back


class ComponentRegistry:
    registry = {
        'none': Component('', [''], ['']),
        'game': ArticleAdjectiveComponent('', Data.game_adjectives, Data.game_types, ['player']),
        'player': ArticleAdjectiveComponent('where you play', Data.player_adjectives, Data.player_professions, ['player_from_local']),
        'player_from_local': Component('from', Data.player_from_local, ['player_from_world']),
        'player_from_world': Component('', Data.player_from_world, ['goal_verb'], ','),
        'goal_verb': Component('trying to', Data.goal_verb, ['goal_target']),
        'goal_target': Component('', Data.goal_target, ['bad_guy_interaction']),
        'bad_guy_interaction': Component('while', Data.bad_guy_interaction, ['bad_guy']),
        'bad_guy': ArticleAdjectiveComponent('', Data.bad_guy_adjective, Data.bad_guy_type, ['bad_guy_from']),
        'bad_guy_from': Component('from', Data.bad_guy_from, ['none'])
    }

    @staticmethod
    def get_traversed_sentence(seed=-1):
        if seed >= 0:
            random.seed(seed)
        next_type = 'game'
        build_string = ''
        random_number = random.randint(0,1000)
        while next_type != '':
            current_component = ComponentRegistry.registry[next_type]
            build_string += current_component.get_a_descriptor(random_number) + ' '
            next_type = current_component.get_next_type(random_number)
            random_number = random.randint(0, 1000)
        return build_string.strip()


