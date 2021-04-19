from json_io import *
from nlp.enumerate_new_commands import *

#List of commands
commands = ["pick rose"]

"""

print("ANNOTATING SYNSETS...")
word_senses = annotate_synsets(commands)
confirmed_hypernyms = {}
confirmed_hyponyms = {}

for word in word_senses:
    word_sense = wn.synset(word_senses[word])
    print("PICKING HYPERNYMS OF {word}...".format(word=word_sense.name().upper()))
    confirmed_hypernyms[word] = confirm_hyponyms(word, word_sense, do_hypernyms_instead=True)
    print("PICKING HYPONYMS OF {word}...".format(word=word_sense.name().upper()))
    confirmed_hyponyms[word] = confirm_hyponyms(word, word_sense)

print("ANNOTATIONS COMPLETED! SAVING TO LOCAL...")
save_to_file(word_senses, confirmed_hyponyms, confirmed_hypernyms)
print("SAVING DONE!")
"""
input_file_path = "word-sense-annotations.json"
senses, hypernyms, hyponyms = read_from_file(input_file_path)

alternative_commands = {}
for command in commands:
    alternative_commands.update(enumerate_alternatives(command, senses, hypernyms, hyponyms))

#for alt_sent in alternative_commands:
#    print("%s => %s" %(alt_sent, alternative_commands[alt_sent]))

print("Congratulations, you can now handle", len(alternative_commands.keys()),"commands instead of just", len(commands))
