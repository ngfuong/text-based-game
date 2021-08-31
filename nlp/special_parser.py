from nltk.corpus import stopwords
from nltk import word_tokenize
from string import punctuation
# Install pymagnitude with pip3
from pymagnitude import Magnitude
import numpy as np
# Define VECTORS as global var
VECTORS = Magnitude("/home/ngfuong/programming/text-based-game/nlp/glove.6B.300d.magnitude")


def construct_sentence_vector(command):
    """Sentence vector is constructed by taking the component-wide avg of words in the command.
    Sent vector has the same length as a word vector."""
    sentence_vector = np.zeros(shape=(VECTORS.dim,))
    for word in command.split():
        word_vector = VECTORS.query(word)
        sentence_vector += word_vector

    sentence_vector = sentence_vector/len(command.split())
    return sentence_vector


def find_most_similar(user_command, known_commands):
    """This finds the most similar command to the player's input in the set of known commands."""
    user_command_vect = construct_sentence_vector(user_command)
    known_commands_vects = [VECTORS.similarity(user_command_vect, construct_sentence_vector(command))
                            for command in known_commands]
    max_score = np.max(known_commands_vects)
    threshold = 0.6  # Edit threshold to ensure accuracy
    if max_score < threshold:
        return None

    most_similar_cmd = known_commands[known_commands_vects.index(max_score)]

    return most_similar_cmd


def tokenize_and_clean(command):
    """Clean command and return a tokenized list."""
    tokens = word_tokenize(command)
    tokens = [token.lower() for token in tokens]

    # Remove punctuations
    table = str.maketrans('', '', punctuation.replace(',', ''))
    tokens = [token.translate(table) for token in tokens]

    # Remove useless tokens
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token.isalpha() and token not in stop_words]

    return tokens


def clean(command):
    """Return a cleaned command"""
    return " ".join(tokenize_and_clean(command))
