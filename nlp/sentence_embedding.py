from pymagnitude import Magnitude
import numpy as np
from generate_commands import generate_commands

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

  # TODO - Do something
  return sentence_vector


def find_most_similar_command(user_command, known_commands, vectors):
  # TODO - Do something
  return known_commands[0]


vectors = Magnitude("glove.6B.300d.magnitude")
construct_sentence_vector("get fish", vectors)
commands = [
  "catch fish",
  "pick rose"
]
print(generate_commands(commands))
