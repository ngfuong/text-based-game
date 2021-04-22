from pymagnitude import *
import numpy as np
from nlp.generate_commands import *

"""
## Finding the most similar command
Take in the player's command and find the most similar command in the set of known commands.  

=> construct a sentence embedding for a command by taking the component wide average of words in the command.
The sentence embedding will have the same length as a word embedding.
You can compare a player's command against each of the known commands by constructing vectors for all of them,
and then using Magnitude's `similarity` function.
"""


def construct_sentence_vector(command, vectors):
    sentence_vector = np.zeros(shape=(vectors.dim,))
    for word in command.split():
        word_vector = vectors.query(word)
        sentence_vector += word_vector

    sentence_vector = sentence_vector/len(command.split())
    return sentence_vector


def find_most_similar_command(user_command, known_commands, vectors):
    user_command_vect = construct_sentence_vector(user_command, vectors)
    known_commands_vects = [vectors.similarity(user_command_vect, construct_sentence_vector(command, vectors))
                            for command in known_commands]
    max_score = np.max(known_commands_vects)
    most_similar_cmd = known_commands[known_commands_vects.index(max_score)]

    return most_similar_cmd


# Edit vectors file path accordingly
vectors = Magnitude("/home/ngfuong/programming/text-based-game/nlp/glove.6B.300d.magnitude")
# construct_sentence_vector("get fish", vectors)
commands = [
  "catch fish",
  "pick rose"
]
command_dict = generate_commands(commands)
# print(find_most_similar_command("catch a fish", command_dict.values(), vectors))
print(command_dict.values())