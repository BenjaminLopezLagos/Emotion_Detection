from json import load
import nltk
import functools
import re
from abc import ABC
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import wordnet
from transformers import pipeline
import torch
import fuzzy_functions as fuzzy

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('corpus')
nltk.download('wordnet')
nltk.download('vader_lexicon')
nltk.download('averaged_perceptron_tagger')


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
        with open(lex_file, 'r') as json_file:
            self.lexicon_dict = load(json_file)

    def execute(self, phrase):
        print(self.lexicon.shape)
        tokens = phrase.clean_phrase()
        print(tokens)
        emotions = {'fear': 0.0, 'anger': 0.0, 'anticipation': 0.0, 'trust': 0.0,
                    'surprise': 0.0, 'positive': 0.0, 'negative': 0.0, 'sadness': 0.0,
                    'disgust': 0.0, 'joy': 0.0}
        # emo tokens means words that have emotions in the lexicon
        n_emo_tokens = 0
        for w in tokens:
            # in progress, it's supposed to boost words that have "very" as prefix
            multiplier = 1
            # If there's a particular word inside the token
            if w.find("not") != -1:
                w = change_negative_word_to_antonym(w)
            if w.find("very") != -1:
                multiplier = 2
                w = remove_very_from_token(w)
            """
            if self.lexicon["word"].str.contains(w).any():
                word_lex_df = self.lexicon.query("word == @w & is_present > 0")
                for index, row in word_lex_df.iterrows():
                    emotions[row["emotion"]] += 1 * multiplier
            """
            if self.lexicon_dict.get(w):
                n_emo_tokens += 1
                w_emotions = self.lexicon_dict[w]
                for i in w_emotions:
                    emotions[i] += 1 * multiplier
        try:
            emotions = normalize_emotion_dict(emotions, n_emo_tokens)
            return apply_fuzziness_to_emotions(emotions)
        except ZeroDivisionError:
            # returns the same emotion dict in the case that it only contains 0's.
            return apply_fuzziness_to_emotions(emotions)


def normalize_emotion_dict(emotions: dict, n: int):
    for key in emotions.keys():
        emotions[key] = float(emotions[key]) / float(n)
    return emotions


def apply_fuzziness_to_emotions(emotions: dict):
    for key in emotions.keys():
        emotion_value = emotions[key]
        emo_degrees = {'low': fuzzy.u_sigmoid(emotion_value, -10.0, 0.3),
                       'medium': fuzzy.u_generalized_bell(emotion_value, 0.15, 5.0, 0.5),
                       'high': fuzzy.u_sigmoid(emotion_value, 10.0, 0.7)}
        emotions[key] = emo_degrees
    return emotions


class VADER(DetectionStrategy):
    def execute(self, phrase):
        analyzer = SentimentIntensityAnalyzer()
        return analyzer.polarity_scores(phrase.text)


class Transformers(DetectionStrategy):
    def execute(self, phrase):
        ekman = pipeline('sentiment-analysis', model='arpanghoshal/EkmanClassifier')
        results = ekman(phrase.text)
        # esto retorna un diccionario {'emocion': string, 'puntaje': float}
        return ekman(phrase.text)[0]


"""
Utilizar en main como:
    phrase = Phrase("I am not dumb and she is stupid. The dog is rapping.")
    input_tags = []
    for x in phrase.raw_tokens:
        input_tags.append(x[1])
    input_stream = InputStream(' '.join(input_tags))
"""


class Phrase:
    def __init__(self, text):
        self.text = text
        self.raw_tokens = nltk.pos_tag(word_tokenize(self.decontracted()))
        print(self.raw_tokens)

    def decontracted(self):
        phrase = re.sub(r"n\'t", " " + "not", self.text)
        phrase = re.sub(r"\'re", " " + "are", phrase)
        phrase = re.sub(r"\'s", " " + "is", phrase)
        phrase = re.sub(r"\'d", " " + "would", phrase)
        phrase = re.sub(r"\'ll", " " + "will", phrase)
        phrase = re.sub(r"\'ve", " " + "have", phrase)
        phrase = re.sub(r"\'m", " " + "am", phrase)
        return phrase

    def clean_phrase(self):
        modified_phrase = self.decontracted()
        stop_words = set(stopwords.words('english'))
        stop_words.remove('not')
        stop_words.remove('very')
        stop_words.remove('nor')
        word_tokens = word_tokenize(modified_phrase)
        filtered_sentence = [w.lower() for w in word_tokens if w not in stop_words and w.isalnum()]
        filtered_sentence = [WordNetLemmatizer().lemmatize(w) for w in filtered_sentence]
        filtered_sentence = join_keywords(filtered_sentence)
        for i in range(len(filtered_sentence)):
            if filtered_sentence[i] == "hated":
                # special case where the word "hated" is not correctly lemmatized
                filtered_sentence[i] = "hate"
            if filtered_sentence[i].endswith("ed"):
                filtered_sentence[i] = WordNetLemmatizer().lemmatize(filtered_sentence[i], pos="v")

        return filtered_sentence


# Joins tokens like "not" or "very" with the following word.
def join_keywords(token_list: list):
    index_limit = range(len(token_list) - 1)
    try:
        for i in index_limit:
            if token_list[i].startswith('not') or token_list[i].startswith('very'):
                token_list[i: i + 2] = [functools.reduce(lambda x, y: x + " " + y, token_list[i: i + 2])]
    except IndexError:
        # Might add a fix later but it works for now.
        print("Stopping token joining process.")
    return token_list


# must contain "not" before a word
def change_negative_word_to_antonym(word: str):
    try:
        new_word = word.replace("not", "").strip()
        antonyms = get_antonyms(new_word)
        new_word = antonyms[0]
        return new_word
    except IndexError:
        return word


def remove_very_from_token(word: str):
    new_word = word.replace("very", "").strip()
    return new_word


def get_antonyms(word: str):
    antonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            if lemma.antonyms():
                antonyms.extend([antonym.name() for antonym in lemma.antonyms()])
    return antonyms
