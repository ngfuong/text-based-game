#import nltk
#nltk.download('wordnet')
#nltk.download('punkt')
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

"""
Words can have multiple meanings. WordNet organizes word senses into a structure called synsets.
Each word can have multiple synsets, each synset represents a different meaning of that word.
"""
def get_senses(word):
    """
    Returns a list of senses (synsets) of a word
    """
    word_senses = wn.synsets(word)
    return word_senses


def get_definition(word_sense):
    return word_sense.definition()


def get_synonyms(word_sense):
    synonyms = []
    for lemma in word_sense.lemmas():
        synonym = lemma.name().replace('_', ' ')
        synonyms.append(synonym)
    return synonyms

"""
For example, red is a specific kind of color, or microbe is a kind of organism.
If X is-a Y then X is a hyponym of Y, and Y is a hypernym of X.
So red is a hyponym of color and color is a hypernym of red.
In WordNet, each word sense (synset) has its own hypernyms and hyponyms.
"""
def get_hypernyms(word_sense, depth=5):
    hyper = lambda s: s.hypernyms()
    return list(word_sense.closure(hyper, depth=depth))


def get_hyponyms(word_sense, depth=5):
    hypo = lambda s: s.hyponyms()
    return list(word_sense.closure(hypo, depth=depth))


def annotate_synsets(sentences):
    """
    This function queries WordNet for each word in each sentence in a list of sentences,
    and asks the user to choose the appropriate meaning/synset for the word.
    """
    word_senses = {}
    # Cached selections maps a word string to the previous selection for this word (an int)
    cached_selections = {}

    for i, sent in enumerate(sentences):
        print("-----------\n%s\n-----------" % sent.upper())
        words = word_tokenize(sent.lower())

        for word in words:
            synsets = wn.synsets(word)
            if len(synsets) != 0:
                selection = select_synset(sent, word, synsets, cached_selections)
                if selection != None:
                    cached_selections[word] = selection
                    if selection < len(synsets):
                        s = synsets[selection]
                        word_senses[word] = s.name()
        clear()
    print("===")
    return word_senses


def select_synset(sent, word, synsets, cached_selections):
    """Ask the user to select which sense of the word
       is being used in this sentence."""
    print(word.upper())

    prev_selection = -1
    if word in cached_selections:
        prev_selection = cached_selections[word]

    for choice, s in enumerate(synsets):
        if choice == prev_selection:
            print("*** ", end='')
        print("%d) %s - %s" % (choice, s.name(), s.definition()))

    choice += 1
    if choice == prev_selection:
        print("*** ", end='')
    print("%d) None of these." % choice)

    selection = -1
    while selection == -1:
        try:
            user_input = input(">")
            if user_input.strip() == 'x':
                # The user can press 'x' to exit.
                return None
            if user_input.strip() == '' and prev_selection > -1:
                # The user can press retrun to confirm the previous selection.
                return prev_selection
            selection = int(user_input)
        except:
            selection = -1
        if selection < 0 or selection > len(synsets):
            print("Please select a number between 0-%d, or type 'x' to exit" % len(synsets))
            if prev_selection > -1:
                print("You can also press return to confirm the previous selection (marked by ***).")
        else:
            return selection


def confirm_hyponyms(word, synset, do_hypernyms_instead=False):
    """Ask the user to confirm which of the hyponyms are applicable
       for this sentence."""
    print("{word}".format(word=word.upper()))

    confirmed = []
    if do_hypernyms_instead:
        unconfirmed = synset.hypernyms()
    else:
        unconfirmed = synset.hyponyms()

    while len(unconfirmed) > 0:
        s = unconfirmed.pop(0)
        print("Is {name} an appropriate substitute for {word}? (y/n/x)".format(name=s.name().upper(),
                                                                             word=word.upper()))
        print("It means:", s.definition())
        print("Synonyms are:", get_synonyms(s))
        user_input = ''
        while user_input == '':
            user_input = input(">")
            user_input = user_input.strip()
            if user_input == 'y' or user_input == 'yes':
                confirmed.append(s.name())
                if do_hypernyms_instead:
                    unconfirmed.extend(s.hypernyms())
                else:
                    unconfirmed.extend(s.hyponyms())

            elif user_input == 'n' or user_input == 'no':
                pass
            elif user_input == 'x':
                # The user can press 'x' to exit.
                return confirmed
            else:
                print("Please type 'yes' or 'no' or 'x' to stop confirming for this word")
                user_input = ''
            print()
    return confirmed


