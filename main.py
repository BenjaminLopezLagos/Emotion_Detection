# This is a sample Python script.
import nltk
from EmotionLex import *
from antlr4 import *
from grammar_classes import GrammarLexer
from grammar_classes import GrammarParser
from grammar_classes import GrammarVisitor


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main():
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('corpus')
    nltk.download('wordnet')
    nltk.download('vader_lexicon')

    algorithm = NRCLex()
    emotion_lex = EmotionLex(algorithm)

    phrase = Phrase("He abandoned.")
    input_stream = InputStream(phrase.text)
    lexer = GrammarLexer.GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser.GrammarParser(stream)
    tree = parser.sentence()
    print(tree)

    emotions = emotion_lex.detect_emotion(phrase)

    print(emotions)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
