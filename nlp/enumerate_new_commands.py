from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nlp.manually_annotate import get_synonyms
import itertools


def get_alternatives(word, word_senses, confirmed_hypernyms, confirmed_hyponyms):
    """
    Create a list of reasonable alternative for a word by listing out the synonyms for its word sense, and for its hyponyms and hypernyms
    """
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
    """
    words = word_tokenize(sentence.lower())
    # 2-D list
    alternatives_per_word = []
    for word in words:
        alternatives = get_alternatives(word, word_senses, confirmed_hypernyms, confirmed_hyponyms)
        alternatives_per_word.append(alternatives)

    # combination of 2-D lists
    alternative_to_original = {}
    for words in list(itertools.product(*alternatives_per_word)):
        alt_sent = " ".join(words)
        alternative_to_original[alt_sent] = sentence
    return alternative_to_original
