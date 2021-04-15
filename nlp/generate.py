from . import *
from .manually_annotate import *
from .json_io import *

#List of commands
commands = ["pick rose", "give fish to troll"]

print("ANNOTATING SYNSETS...")
word_senses = annotate_synsets(commands)
confirmed_hyponyms = {}
confirmed_hypernyms = {}

for word in word_senses:
    print("First, pick the word sense for the word '%s'..." % word.upper())
    word_sense = wn.synset(word_senses[word])
    print("Next, pick which hypernyms of %s we should allow players to use..." % word_sense.name().upper())
    confirmed_hypernyms[word] = confirm_hyponyms(word, word_sense, do_hypernyms_instead=True)
    print("Finally, pick which hyponyms of %s we should allow players to use..." % word_sense.name().upper())
    confirmed_hyponyms[word] = confirm_hyponyms(word, word_sense)

print("You've done annotating!")
save_to_file(word_sense, confirmed_hyponyms, confirmed_hypernyms)
