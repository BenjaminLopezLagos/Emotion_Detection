import json
import nltk
import re
from abc import ABC
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class EmotionLex:
    def __init__(self, detection_strategy):
        self.detection_strategy = detection_strategy

    def detect_emotion(self, phrase):
        return self.detection_strategy.execute(phrase)


class DetectionStrategy(ABC):
    def execute(self, phrase):
        pass


class NRCLex(DetectionStrategy):
    def __init__(self, lex_file='nrc_en.json'):
        self.lexicon = pd.read_csv("nrclex.txt", sep="	", header=None, names=["word", "emotion", "is_present"])
        # with open(lex_file, 'r') as json_file:
        #    self.lexicon = json.load(json_file)

    def execute(self, phrase):
        # df = pd.read_csv("nrclex.txt", sep="	", header=None, names=["word", "emotion", "is_present"])
        unique_elements = self.lexicon["word"].unique()
        print(self.lexicon.shape)
        tokens = phrase.clean_phrase()
        print(tokens)
        emotions = {'fear': 0.0, 'anger': 0.0, 'anticipation': 0.0, 'trust': 0.0,
                    'surprise': 0.0, 'positive': 0.0, 'negative': 0.0, 'sadness': 0.0,
                    'disgust': 0.0, 'joy': 0.0}
        for w in tokens:
            if self.lexicon["word"].str.contains(w).any():
                word_lex_df = self.lexicon.query("word == @w & is_present > 0")
                # print(word_lex_df.head())
                for index, row in word_lex_df.iterrows():
                    emotions[row["emotion"]] += 1

        return emotions


class VADER(DetectionStrategy):
    def execute(self, phrase):
        analyzer = SentimentIntensityAnalyzer()
        return analyzer.polarity_scores(phrase.text)


class Phrase:
    def __init__(self, text):
        self.text = text

    def decontracted(self):
        phrase = re.sub(r"n\'t", " "+"not", self.text)
        phrase = re.sub(r"\'re", " "+"are", phrase)
        phrase = re.sub(r"\'s", " "+"is", phrase)
        phrase = re.sub(r"\'d", " "+"would", phrase)
        phrase = re.sub(r"\'ll", " "+"will", phrase)
        phrase = re.sub(r"\'ve", " "+"have", phrase)
        phrase = re.sub(r"\'m", " "+"am", phrase)
        return phrase

    def clean_phrase(self):
        modified_phrase = self.decontracted()
        stop_words = set(stopwords.words('english'))
        stop_words.remove('not')
        word_tokens = word_tokenize(modified_phrase)
        filtered_sentence = [w.lower() for w in word_tokens if w not in stop_words and w.isalnum()]
        filtered_sentence = [WordNetLemmatizer().lemmatize(w) for w in filtered_sentence]

        return filtered_sentence
