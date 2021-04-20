from pymagnitude import *
from generate_commands import *

# FOR YOU TO DO: Write these function
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