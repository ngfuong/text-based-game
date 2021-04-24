from allennlp.predictors.predictor import Predictor


def verb_object_pairs(sentence):
    print('Sentence:', sentence)

    predictor = Predictor.from_path(
        "https://storage.googleapis.com/allennlp-public-models/biaffine-dependency-parser-ptb-2020.04.06.tar.gz")
    prediction = predictor.predict(sentence=sentence)

    words = prediction['words']
    pred_depends = prediction['predicted_dependencies']
    pred_heads = prediction['predicted_heads']

    pairs = []
    for i in range(len(words)):
        if pred_depends[i] == 'dobj':
            verb = words[pred_heads[i]-1]
            direct_object = words[i]
            pairs.append((verb, direct_object))

    return pairs


def conference_resolution(sentence):
    print('Sentence:', sentence)

    predictor = Predictor.from_path(
        "https://storage.googleapis.com/allennlp-public-models/coref-spanbert-large-2021.03.10.tar.gz")
    prediction = predictor.predict(document=sentence)
    print(prediction)

    clusters = prediction['clusters']
    words = prediction['document']
    for cluster in clusters:
        entity_indices, pronoun_indices = cluster
        entity_str = words[entity_indices[0]:entity_indices[1]+1]
        pronoun_str = words[pronoun_indices[0]:pronoun_indices[1]+1]
        print("{pronoun} references {entity}".format(pronoun=pronoun_str, entity=entity_str))


print(conference_resolution("Take the apple from the table and eat it."))

