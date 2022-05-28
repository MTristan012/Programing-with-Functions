from sentences import get_determiner, get_noun, get_preposition, get_verb
import random
import pytest

def test_get_determiner():

    single_determiners = ["a", "one", "the"]

    for _ in range(4):
        word = get_determiner(1)
        assert word in single_determiners

    plural_determiners = ["two", "some", "many", "the"]

    for _ in range(4):
        word = get_determiner(2)
        assert word in plural_determiners

def test_get_noun():

    single_nouns = ["bird", "boy", "car", "cat",
                    "child", "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(10):
        noun = get_noun(1)
        assert noun in single_nouns

    plural_nouns = ["birds", "boys", "cars", "cats",
                          "children", "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(10):
        noun = get_noun(2)
        assert noun in plural_nouns

def test_get_verb():

    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
                  "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(10):
        verb = get_verb(1, "past")
        assert verb in past_verbs

    present_and_singular_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                                  "runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(10):
        verb = get_verb(1, "present")
        assert verb in present_and_singular_verbs
    
    present_and_plural_verbs = ["drink", "eat", "grow", "laugh", "think",
                                "run", "sleep", "talk", "walk", "write"]

    for _ in range(10):
        verb = get_verb(2, "present")
        assert verb in present_and_plural_verbs
    
    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
                  "will think", "will run", "will sleep", "will talk",
                  "will walk", "will write"]

    for _ in range(10):
        verb = get_verb(1,"future")
        assert verb in future_verbs

def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]

    for _ in range(30):
        preposition = get_preposition()
        assert preposition in prepositions

def test_get_prepositional_phrase():
    test_get_preposition()
    test_get_determiner()
    test_get_noun()

pytest.main(["-v", "--tb=line", "-rN", __file__])
