import random


def main():

    determiner = get_determiner(1)
    noun = get_noun(1)
    verb = get_verb(1, "past")
    prepositional_phrase = get_prepositional_phrase(1)
    prepositional_phrase_two = get_prepositional_phrase(1)
    print(f"{determiner} {noun} {verb} {prepositional_phrase} {prepositional_phrase_two}")
    determiner = get_determiner(1)
    noun = get_noun(1)
    verb = get_verb(1, "present")
    prepositional_phrase = get_prepositional_phrase(1)
    prepositional_phrase_two = get_prepositional_phrase(1)
    print(f"{determiner} {noun} {verb} {prepositional_phrase} {prepositional_phrase_two}")
    determiner = get_determiner(1)
    noun = get_noun(1)
    verb = get_verb(1, "future")
    prepositional_phrase = get_prepositional_phrase(1)
    prepositional_phrase_two = get_prepositional_phrase(1)
    print(f"{determiner} {noun} {verb} {prepositional_phrase} {prepositional_phrase_two}")
    determiner = get_determiner(2)
    noun = get_noun(2)
    verb = get_verb(2, "past")
    prepositional_phrase = get_prepositional_phrase(2)
    prepositional_phrase_two = get_prepositional_phrase(2)
    print(f"{determiner} {noun} {verb} {prepositional_phrase} {prepositional_phrase_two}")
    determiner = get_determiner(2)
    noun = get_noun(2)
    verb = get_verb(2, "present")
    prepositional_phrase = get_prepositional_phrase(2)
    prepositional_phrase_two = get_prepositional_phrase(2)
    print(f"{determiner} {noun} {verb} {prepositional_phrase} {prepositional_phrase_two}")
    determiner = get_determiner(2)
    noun = get_noun(2)
    verb = get_verb(2, "future")
    prepositional_phrase = get_prepositional_phrase(2)
    prepositional_phrase_two = get_prepositional_phrase(2)
    print(f"{determiner} {noun} {verb} {prepositional_phrase} {prepositional_phrase_two}")

def get_determiner(quantity):

    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_noun(quantity):

    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    noun = random.choice(nouns)
    return noun


def get_verb(quantity, tense):

    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                 "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think",
                 "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk",
                 "will walk", "will write"]
    verb = random.choice(verbs)
    return verb


def get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)
    return preposition

def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    prepositional_phrase = preposition + " " + determiner + " " + noun
    return prepositional_phrase

main()