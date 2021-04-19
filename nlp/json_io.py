import json


def save_to_file(word_senses, confirmed_hyponyms, confirmed_hypernyms):
    """
    This function saves your annotations to a local file.
    :param word_senses:
    :param confirmed_hyponyms:
    :param confirmed_hypernyms:
    :return:
    """
    output_file = 'word-sense-annotations.json'
    output_json = {'senses': word_senses, 'hyponyms': confirmed_hyponyms, 'hypernyms': confirmed_hypernyms}
    with open(output_file, 'w') as f:
        json.dump(output_json, f, ensure_ascii=False, sort_keys=True, indent=4)


def read_from_file(input_file_path):
    """
    This function reads your annotations from a local file.
    :return:
    """
    input_file = input_file_path
    with open(input_file, 'r') as f:
        data = json.load(f)

    word_senses = data['senses']
    confirmed_hypernyms = data['hypernyms']
    confirmed_hyponyms = data['hyponyms']

    return word_senses, confirmed_hypernyms, confirmed_hyponyms
