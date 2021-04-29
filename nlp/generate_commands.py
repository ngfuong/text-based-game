import itertools
import json
import os
from nlp.manually_annotate import *
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize


def save_to_file(word_senses, confirmed_hypernyms, confirmed_hyponyms, file_path="/home/ngfuong/programming/text-based-game/nlp/word-annotations.json"):
    """
    This function saves your annotations to a local file.
    :param word_senses:
    :param confirmed_hypernyms:
    :param confirmed_hyponyms:
    :return:
    """
    output_json = {'senses': word_senses, 'hypernyms': confirmed_hypernyms, 'hyponyms': confirmed_hyponyms}
    with open(file_path, 'w') as f:
        json.dump(output_json, f, ensure_ascii=False, sort_keys=True, indent=4)

    return word_senses, confirmed_hypernyms, confirmed_hyponyms


def read_from_file(input_file_path):
    """This function reads your annotations from a local file."""
    input_file = input_file_path
    with open(input_file, 'r') as f:
        data = json.load(f)

    word_senses = data['senses']
    confirmed_hypernyms = data['hypernyms']
    confirmed_hyponyms = data['hyponyms']

    return word_senses, confirmed_hypernyms, confirmed_hyponyms


def get_alternatives(word, word_senses, confirmed_hypernyms, confirmed_hyponyms):
    """Create a list of reasonable alternative for a word
    by listing out the synonyms for its word sense, and for its hyponyms and hypernyms."""
    alternatives = []
    if word not in word_senses:
        alternatives.append(word)
        return alternatives

    word_sense = wn.synset(word_senses[word])
    alternatives.extend(get_synonyms(word_sense))
    for hypernym in confirmed_hypernyms[word]:
        alternatives.extend(get_synonyms(wn.synset(hypernym)))
    for hyponym in confirmed_hyponyms[word]:
        alternatives.extend(get_synonyms(wn.synset(hyponym)))

    return alternatives


def enumerate_alternatives(sentence, word_senses, confirmed_hypernyms, confirmed_hyponyms):
    """
    Enumerate all of the sentences that can result
    by taking any combination of the alternates for each word in the sentence
    :return: A list of alternative commands
    """
    words = word_tokenize(sentence.lower())
    # 2-D list
    alternatives_per_word = []
    for word in words:
        alternatives = get_alternatives(word, word_senses, confirmed_hypernyms, confirmed_hyponyms)
        alternatives_per_word.append(alternatives)

    # combination of 2-D lists
    alternatives = list()
    for words in list(itertools.product(*alternatives_per_word)):
        alt_sent = " ".join(words)
        alternatives.append(alt_sent)

    return alternatives


def generate_annotations(commands):
    print("ANNOTATING SYNSETS...")
    confirmed_word_senses = annotate_synsets(commands)
    confirmed_hypernyms = {}
    confirmed_hyponyms = {}

    for word in confirmed_word_senses:
        word_sense = wn.synset(confirmed_word_senses[word])
        print("PICKING HYPERNYMS OF {word}...".format(word=word_sense.name().upper()))
        confirmed_hypernyms[word] = confirm_hyponyms(word, word_sense, do_hypernyms_instead=True)
        print("PICKING HYPONYMS OF {word}...".format(word=word_sense.name().upper()))
        confirmed_hyponyms[word] = confirm_hyponyms(word, word_sense)

    return confirmed_word_senses, confirmed_hypernyms, confirmed_hyponyms


def generate_command_dict(commands, file_path="/home/ngfuong/programming/text-based-game/nlp/word-annotations.json"):
    """
    Generate alternative commands a dictionary of {main-commands:list of alternatives}
    :return: a dictionary with keys as input commands and values as list of respective alternative commands.
    """
    try:
        filesize = os.path.getsize(file_path)
        if filesize == 0:
            # print("NO ANNOTATION DATA.", end=' ')
            senses, hypernyms, hyponyms = generate_annotations(commands)
            save_to_file(senses, hypernyms, hyponyms, file_path)
        else:
            # print("IMPORTING LOCAL ANNOTATIONS...")
            senses, hypernyms, hyponyms = read_from_file(file_path)
    except OSError:
        print("OSError: File does not exist or inaccessible!")
        return None

    alternative_commands = {
        command: enumerate_alternatives(command, senses, hypernyms, hyponyms)
        for command in commands
    }
    return alternative_commands
