# This is a sample Python script.
import sys

import nltk
from PyQt5 import QtWidgets

from EmotionLex import *
from antlr4 import *
from grammar_classes import GrammarLexer
from grammar_classes import GrammarParser
from grammar_classes import GrammarVisitor

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def processNRCLexer(text):
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('corpus')
    nltk.download('wordnet')
    nltk.download('vader_lexicon')

    algorithm = NRCLex()
    emotion_lex = EmotionLex(algorithm)
    #phrase = Phrase("Pablo is smart and she is stupid. The dog is rapping.")
    phrase = Phrase(text)
    input_tags = []
    for x in phrase.raw_tokens:
        input_tags.append(x[1])
    input_stream = InputStream(' '.join(input_tags))
    lexer = GrammarLexer.GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser.GrammarParser(stream)

    result = parser.start()
    if result.exception is None:
        emotions = emotion_lex.detect_emotion(phrase)
        print(emotions)
    else:
        print("Entrada inválida.")

def processTransformer(text):
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('corpus')
    nltk.download('wordnet')
    nltk.download('vader_lexicon')

    algorithm = Transformers()
    emotion_lex = EmotionLex(algorithm)
    #phrase = Phrase("Pablo is smart and she is stupid. The dog is rapping.")
    phrase = Phrase(text)
    input_tags = []
    for x in phrase.raw_tokens:
        input_tags.append(x[1])
    input_stream = InputStream(' '.join(input_tags))
    lexer = GrammarLexer.GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser.GrammarParser(stream)

    result = parser.start()
    if result.exception is None:
        emotions = emotion_lex.detect_emotion(phrase)
        print(emotions)
    else:
        print("Entrada inválida.")
