import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


class EmotionLex:
    def __init__(self, lex_file='nrc_en.json'):
        with open(lex_file, 'r') as json_file:
            self.lexicon = json.load(json_file)

    def find_emotions(self, phrase):
        phrase.emotions = dict.fromkeys(phrase.emotions, 0.0)
        for w in phrase.tokens:
            if w in self.lexicon:
                word_emotions = self.lexicon[w]
                for e in word_emotions:
                    phrase.emotions[e] += 1


class Phrase:
    def __init__(self, text):
        self.text = text
        self.tokens = Phrase.clean_phrase(text)
        self.emotions = {'fear': 0.0, 'anger': 0.0, 'anticipation': 0.0, 'trust': 0.0,
                         'surprise': 0.0, 'positive': 0.0, 'negative': 0.0, 'sadness': 0.0,
                         'disgust': 0.0, 'joy': 0.0}

    @staticmethod
    def clean_phrase(text):
        text_tokens = []
        stop_words = set(stopwords.words('english'))
        lemmatizer = WordNetLemmatizer()
        word_tokens = word_tokenize(text)
        filtered_sentence = [w.lower() for w in word_tokens if w not in stop_words and w.isalnum()]
        filtered_sentence = [lemmatizer.lemmatize(w) for w in filtered_sentence]
        for w in filtered_sentence:
            text_tokens.append(w)

        return text_tokens
