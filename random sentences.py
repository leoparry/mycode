
name = ['Neha', 'Lee', 'Leo', 'Sam', 'Dad', 'Max']
verb = ['buys', 'let\'s one off on', 'does a BOOM BOOM', 'goes to the toilet on',
        'does a wiggle wiggle on', 'snogs', 'bunjee jumps onto', 'flirts with', 'assasinates', 'get\'s enraged with',
        'investigates the bottom of', 'eats the fleas on', 'eats', 'poos on a', 'throws', 'sexes with']
noun = ['lion', 'bicycle', 'plane', 'grandma', 'big fat ogre', 'hippo', 'computer', 'darth vader','cat', 'blobfish']
from random import randint


def pick(words):
    num_words = len(words)
    num_picked = randint(0, num_words - 1)
    word_picked = words[num_picked]
    return word_picked


while True:
    print(pick(name), pick(verb), 'a', pick(noun), end='.')
    input()
