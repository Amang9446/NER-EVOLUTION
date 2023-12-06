import spacy


def load_model():
    # Load the spaCy model
    nlp = spacy.load('en_core_web_sm')  # Replace 'en' with the name of your trained model
    return nlp
