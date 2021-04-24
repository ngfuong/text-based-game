import torch
import numpy as np
from transformers import BertTokenizer, BertModel
from scipy.spatial.distance import cosine


tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')


def get_tokens_and_embeddings(text):
    inputs_ids = tokenizer.encode(text)
    input_ids = torch.tensor(inputs_ids).unsqueeze(0) # Batch size 1

    token_embeddings, merged_embeddings = model(input_ids)

    # Remove embeddings in the first (CLS token) and last (SEP token) pos
    token_embeddings = token_embeddings.squeeze()[1:-1, :]
    return token_embeddings.detach().numpy()


def token_indexes_for_word(tokens, word):
    """
    Return the token indexes corresponding to the specified word
    :param tokens:
    :param word:
    :return:
    """
    ids = tokenizer.convert_tokens_to_ids(tokens)

    word_ids = tokenizer.convert_tokens_to_ids(tokenizer.tokenize(word))
    word_len = len(word_ids)

    for i in range(len(tokens)-word_len):
        if np.all(np.equal(ids[i:(i+word_len)], word_ids)):
            return list(range(i, i+word_len))
    return None


sentence = "The bat comes out at night to eat mosquitoes."
embeddings = get_tokens_and_embeddings(sentence)
tokens = tokenizer.tokenize(sentence)
mosquitoes_indices = token_indexes_for_word(tokens, "mosquitoes")
print(sentence)
print(tokens)
print("'mosquitoes' is in token pos {pos}".format(pos=mosquitoes_indices))

