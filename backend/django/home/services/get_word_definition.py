from nltk.corpus import wordnet


def get_word_definition(word):
    if " " in word:
        word = word.replace(" ", "_")

    synset_array = wordnet.synsets(word)

    if synset_array:
        return synset_array[0].definition()
    else:
        return "definition not found"
